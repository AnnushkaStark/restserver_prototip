import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse


class SimpleHTTPRequestHendler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed_path = urlparse(self.path)
        if parsed_path == "/api/data":
            self.send_response(200)
            self.send_header("Content_type", "application/json")
            self.end_headers()
            response = {"message": "HelloWorld!"}
            self.wfile.write(json.dumps(response).encode())
        self.send_response(200)
        self.end_headers()

    def do_POST(self) -> None:
        parsed_path = urlparse(self.path)
        if parsed_path == "api/data":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            self.send_response(201)
            self.end_headers()
            response = {"received": post_data.decode()}
            self.wfile.write(json.dumps(response).encode())
        self.send_response(404)
        self.end_headers()
