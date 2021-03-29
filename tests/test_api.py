def test_get_registration_by_patient(app, client):

    resp = client.post("/create-task/")
    assert resp.status_code == 404
