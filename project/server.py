from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import json
import os
import time
import urllib.request
from urllib.error import HTTPError
from urllib.parse import urlencode

PROJECT_DIR = Path(__file__).resolve().parent
GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vScFQTa69dQ0I_tsgRxULCYWoqhsKTsEu-rrbR6uMUYANsbpY49gRUqoTKEXSAzzq4hVEihBVjEJHFe/pub?output=csv"
HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8003"))
SPOTIFY_METADATA_CACHE = {}


class ArchiveHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_DIR), **kwargs)

    def _send_json_error(self, status, message):
        payload = json.dumps({"ok": False, "error": message}).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("X-Content-Type-Options", "nosniff")
        if urlsplit(self.path).path == "/api/google-sheet":
            self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        request_path = urlsplit(self.path)

        if request_path.path == "/api/spotify-metadata":
            values = parse_qs(request_path.query).get("url", [])
            spotify_url = values[0].strip() if values else ""
            try:
                parsed_spotify_url = urlsplit(spotify_url)
                path_parts = parsed_spotify_url.path.strip("/").split("/")
                valid_spotify_url = (
                    parsed_spotify_url.scheme == "https"
                    and parsed_spotify_url.hostname in ("open.spotify.com", "www.open.spotify.com")
                    and parsed_spotify_url.port in (None, 443)
                    and not parsed_spotify_url.username
                    and not parsed_spotify_url.password
                    and len(path_parts) == 2
                    and path_parts[0] == "track"
                    and len(path_parts[1]) == 22
                    and path_parts[1].isalnum()
                )
            except ValueError:
                valid_spotify_url = False
                path_parts = []
            if not valid_spotify_url:
                self._send_json_error(400, "Invalid Spotify track URL")
                return

            track_id = path_parts[1]
            normalized_url = f"https://open.spotify.com/track/{track_id}"
            cached = SPOTIFY_METADATA_CACHE.get(normalized_url)
            if cached and cached[0] > time.time():
                self._send_json(cached[1])
                return

            try:
                oembed_query = urlencode({"url": normalized_url})
                oembed_request = urllib.request.Request(
                    f"https://open.spotify.com/oembed?{oembed_query}",
                    headers={"User-Agent": "ForTheRecord/1.0"},
                )
                with urllib.request.urlopen(oembed_request, timeout=12) as response:
                    oembed = json.loads(response.read(256_000).decode("utf-8"))
                title = oembed.get("title") if isinstance(oembed, dict) else None
                if not isinstance(title, str) or not title.strip():
                    self._send_json_error(502, "Spotify track metadata is unavailable")
                    return
                payload = {"ok": True, "spotifyId": track_id, "spotifyUrl": normalized_url, "title": title.strip()}
                SPOTIFY_METADATA_CACHE[normalized_url] = (time.time() + 86400, payload)
                self._send_json(payload)
            except HTTPError as error:
                status = 404 if error.code == 404 else 429 if error.code == 429 else 502
                self._send_json_error(status, "Spotify track metadata is unavailable")
            except Exception:
                self._send_json_error(502, "Spotify track metadata is unavailable")
            return

        if request_path.path == "/api/google-drive-photo":
            file_id = parse_qs(request_path.query).get("id", [""])[0]
            if not file_id or any(
                char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
                for char in file_id
            ):
                self._send_json_error(400, "Invalid Google Drive file ID")
                return

            saw_non_image_response = False
            for image_url in (
                f"https://drive.google.com/uc?export=download&id={file_id}",
                f"https://drive.google.com/thumbnail?id={file_id}&sz=w1600",
            ):
                request = urllib.request.Request(
                    image_url, headers={"User-Agent": "Mozilla/5.0"}
                )
                try:
                    with urllib.request.urlopen(request, timeout=20) as response:
                        candidate = response.read()
                        candidate_type = response.headers.get_content_type()
                except Exception:
                    continue

                if candidate_type.startswith("image/") and candidate:
                    self.send_response(200)
                    self.send_header("Content-Type", candidate_type)
                    self.send_header("Content-Length", str(len(candidate)))
                    self.send_header("Cache-Control", "public, max-age=3600")
                    self.send_header("X-Content-Type-Options", "nosniff")
                    self.end_headers()
                    self.wfile.write(candidate)
                    return
                saw_non_image_response = True

            if saw_non_image_response:
                self._send_json_error(415, "Google Drive resource is not an image")
            else:
                self._send_json_error(502, "Google Drive image is unavailable")
            return

        if request_path.path == "/api/google-sheet":
            try:
                with urllib.request.urlopen(GOOGLE_SHEET_CSV_URL, timeout=30) as response:
                    payload = response.read()
            except Exception:
                self._send_json_error(502, "Google Sheet CSV is unavailable")
                return

            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        if request_path.path == "/":
            self.path = "/code.html"

        super().do_GET()

    def _send_json(self, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "public, max-age=3600")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    print(f"Listening on {HOST}:{PORT}", flush=True)
    server = ThreadingHTTPServer((HOST, PORT), ArchiveHandler)
    server.serve_forever()
