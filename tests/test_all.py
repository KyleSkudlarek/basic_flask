import json


def test_index(app, client):
    res = client.get('/')
    res_data = res.get_data(as_text=True)
    assert res_data == "This is my first API call!"