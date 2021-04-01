def test_create_task(client):
    resp = client.post("/api/task/")
    assert resp.status_code == 401, "Can't post empty content!"
    resp = client.post("/api/task/", json={"title": "my title", "text": "."})
    assert resp.status_code == 200


def test_get_task(client):
    resp = client.get("/api/task/")
    assert resp.status_code == 200
    print(f"get_task: {resp.json}")