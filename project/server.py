from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json
import urllib.request

PROJECT_DIR = Path(__file__).resolve().parent
GOOGLE_SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vScFQTa69dQ0I_tsgRxULCYWoqhsKTsEu-rrbR6uMUYANsbpY49gRUqoTKEXSAzzq4hVEihBVjEJHFe/pub?output=csv"


class ArchiveHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
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
    server = ThreadingHTTPServer(("127.0.0.1", 8000), ArchiveHandler)
    server.serve_forever()
