import json

import requests

ROOT_ENPOINT = "http://localhost:8000/api/data"


def test_get_data(server_fixture) -> None:
    response = requests.get(ROOT_ENPOINT)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "HelloWorld!"


def test_post_data(server_fixture) -> None:
    data = {"message": "HelloServer"}
    response = requests.post(ROOT_ENPOINT)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["received"] == json.dumps(data)
