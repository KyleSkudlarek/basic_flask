import json


def test_index(app, client):
    response = client.get('/player/kyle')
    response_json = response.json
    assert response_json == {"names":[["Kyle",9000]]}