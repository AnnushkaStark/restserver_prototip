import requests

ROOT_ENDPOINT = "http://localhost:8000/api/files"
TEST_FILE_NAME = "testfile.txt"


def test_get_files(server_fixture) -> None:
    response = requests.get(ROOT_ENDPOINT)
    assert response.status_code == 200
    response_data = response.json()
    assert ["files"] in response_data


def test_upload_file(server_fixture) -> None:
    with open(TEST_FILE_NAME, "w") as f:
        f.write("this is test file")
    with open(TEST_FILE_NAME, "rb") as f:
        response = requests.post(f"{ROOT_ENDPOINT}/upload", data=f)
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["message"] == "File uploaded succsessfuly"


def test_delete(server_fixture):
    endpoint = f"{ROOT_ENDPOINT}/delete/{TEST_FILE_NAME}"
    response = requests.delete(endpoint)
    assert response.status_code == 204
