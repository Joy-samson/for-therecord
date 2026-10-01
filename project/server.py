from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json
import os
import urllib.request

PROJECT_DIR = Path(__file__).resolve().parent
GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vScFQTa69dQ0I_tsgRxULCYWoqhsKTsEu-rrbR6uMUYANsbpY49gRUqoTKEXSAzzq4hVEihBVjEJHFe/pub?output=csv"


class ArchiveHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/google-drive-photo"):
            from urllib.parse import parse_qs, urlparse

            file_id = parse_qs(urlparse(self.path).query).get("id", [""])[0]
            if not file_id or any(char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for char in file_id):
                self.send_error(400, "Invalid Google Drive file ID")
                return
            try:
                payload = b""
                content_type = ""
                for image_url in (
                    f"https://drive.google.com/uc?export=download&id={file_id}",
                    f"https://drive.google.com/thumbnail?id={file_id}&sz=w1600",
                ):
                    request = urllib.request.Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
                    try:
                        with urllib.request.urlopen(request, timeout=20) as response:
                            candidate = response.read()
                            candidate_type = response.headers.get_content_type()
                        if candidate_type.startswith("image/"):
                            payload = candidate
                            content_type = candidate_type
                            break
                    except Exception:
                        continue
                if not content_type.startswith("image/"):
                    self.send_error(415, "Google Drive resource is not an image")
                    return
                self.send_response(200)
                self.send_header("Content-Type", content_type)
                self.send_header("Cache-Control", "public, max-age=3600")
                self.send_header("X-Content-Type-Options", "nosniff")
                self.end_headers()
                self.wfile.write(payload)
                return
            except Exception as exc:
                self.send_error(502, f"Google Drive image unavailable: {exc}")
                return

        if self.path == "/api/google-sheet":
            try:
                with urllib.request.urlopen(GOOGLE_SHEET_CSV_URL, timeout=30) as response:
                    payload = response.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/csv; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(payload)
                return
            except Exception as exc:
                self.send_response(502)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": str(exc)}).encode("utf-8"))
                return

        super().do_GET()

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", int(os.environ.get("PORT", "8000"))), ArchiveHandler)
    server.serve_forever()
