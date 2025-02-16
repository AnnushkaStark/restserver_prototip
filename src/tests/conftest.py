from http.server import HTTPServer

import pytest

from handlers.main import RestserverHandler


@pytest.fixture(scope="module")
def server_fixture():
    server_address = ("", 8000)
    print("server run")
    test_server = HTTPServer(server_address, RestserverHandler)
    test_server.serve_forever()
    yield
    print("server stop")
    test_server.shutdown()
