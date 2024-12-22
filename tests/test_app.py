from flask.testing import FlaskClient


def test_home_message(client: FlaskClient):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json == {"message": "hello world 2"}
