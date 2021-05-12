import pytest


# https://docs.pytest.org/en/stable/reference.html#pytest-fixture
@pytest.fixture(autouse=True, name="login")  # set fixture name, and will activate
def test_login(client):
    # resp = client.post("/sessions/")
    # assert resp.status_code == 401, "Can't post empty content!"
    resp = client.post("/sessions/", json={"name": "zhang three", "password": "don't guess", "user_role": 1})
    assert resp.status_code == 200


def test_get_session(login, client):
    resp = client.get("/sessions/111")
    assert resp.status_code == 200
    print(f"get_session: {resp.json}")

def test_logout(login, client):
    resp = client.delete("/sessions/111")
    assert resp.status_code == 200
    print(f"logout: {resp.json}")