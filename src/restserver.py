from http.server import HTTPServer

from handlers.main import RestserverHandler


def run(
    server_class=HTTPServer, handler_class=RestserverHandler, port: int = 8000
) -> None:
    server_adress = (" ", 8000)
    http_server = server_class(server_adress, handler_class)
    print(f"Starting server on port {port}")
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == "__main__":
    run()
