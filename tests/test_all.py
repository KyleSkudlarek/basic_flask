import json


def test_get_player(app, client):
    response = client.get('/api/players/aardsda01')
    response_json = response.json

    expected_response_json = {'players': [{'playerId': 'aardsda01', 'birthYear': 1981, 'birthMonth': 12, 'birthDay': 27, 'birthCountry': 'USA', 'birthState': 'CO', 'birthCity': 'Denver', 'deathYear': None, 'deathMonth': None, 'deathDay': None, 'deathCountry': '', 'deathState': '', 'deathCity': '', 'nameFirst': 'David', 'nameLast': 'Aardsma', 'nameGiven': 'David Allan', 'weight': 215, 'height': 75, 'bats': 'R', 'throws': 'R', 'debut': '2004-04-06', 'finalGame': '2015-08-23', 'retroID': 'aardd001', 'bbrefID': 'aardsda01'}]}

    assert response_json == expected_response_json


def test_get_players(app, client):
    response = client.get('/api/players')
    response_json = response.json
    num_players = len(response_json.get('players'))

    expected_num_players = 19370

    assert num_players == expected_num_players


def test_add_height(app, client):
    response = client.put('/api/players/aardsda01/height')
    response_json = response.json
    print(response_json)

    expected_response_json = ["Success", 200]

    assert response_json == expected_response_json


def test_add_weight(app, client):
    response = client.put('/api/players/aardsda01/weight')
    response_json = response.json
    print(response_json)

    expected_response_json = ["Success", 200]

    assert response_json == expected_response_json