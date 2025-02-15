import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse


class FileRequestHandler(BaseHTTPRequestHandler):
    def file_GET(self) -> None:
        parsed_path = urlparse(self.path)
        if parsed_path == "/api/file":
            files = os.listdir(".")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"files": files}
            self.wfile.write(json.dumps(response).encode())
        self.send_response(404)
        self.end_headers()

    def file_POST(self) -> None:
        parsed_path = urlparse(self.path)
        if parsed_path == "/api/file/upload":
            content_length = int(self.headers["Content-Length"])
            file_data = self.rfile.read(content_length)
            with open("uploaded_file", "wb") as f:
                f.write(file_data)
            self.send_response(201)
            self.end_headers()
            response = {"message": "File uploaded succsessfuly"}
            self.wfile.write(json.dumps(response).encode())
        self.send_response(404)
        self.end_headers()

    def file_DELETE(self) -> None:
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith("/api/file/delete"):
            filename = parsed_path.path.split("/")[-1]
            try:
                os.remove(filename)
                self.send_response(204)
                self.end_headers()
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
        self.send_response(404)
        self.end_headers()
