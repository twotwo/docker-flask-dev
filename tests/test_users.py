import pytest


# https://docs.pytest.org/en/stable/reference.html#pytest-fixture
@pytest.fixture(autouse=True, name="create_user")  # set fixture name, and will activate
def test_create_user(client):
    resp = client.post("/users/")
    assert resp.status_code == 401, "Can't post empty content!"
    resp = client.post("/users/", json={"name": "zhang three", "password": "don't guess", "user_role": 1})
    assert resp.status_code == 200


def test_get_user(create_user, client):
    resp = client.get("/users/")
    assert resp.status_code == 200
    print(f"get_user: {resp.json}")

def test_user(create_user, client):
    resp = client.get("/users/1")
    assert resp.status_code == 200
    resp = client.put("/users/1")
    assert resp.status_code == 200
    resp = client.delete("/users/1")
    assert resp.status_code == 200