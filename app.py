from flask import Flask, request, jsonify
import mysql.connector
import logging
import os

cnx = mysql.connector.connect(user='kyle', password='KJSkud26',
                              host='127.0.0.1',
                              database='main',
                              port=3306,
                              autocommit=True)
app = Flask(__name__)
logging.basicConfig(filename=os.path.join(app.root_path, 'logs', 'app.log'), level=logging.INFO)


@app.route('/api/players/<playerID>/weight', methods=["PUT"])
def add_weight(playerID):
    """ This API route increments the playerID weight by 1 """
    app.logger.info(f"PUT /api/players/{playerID}/weight")

    # Update player weight
    cursor = cnx.cursor()
    query = f"UPDATE players Set weight = weight +1 WHERE playerID='{playerID}';"
    app.logger.info(f"Querying database: {query}")
    cursor.execute(query)
    cursor.close()
    response = ("Success", 200)
    app.logger.info(f"Returning response: {response}")
    return jsonify(response)


@app.route('/api/players/<playerID>/height', methods=["PUT"])
def add_height(playerID):
    """ This API route increments the playerID height by 1 """
    app.logger.info(f"PUT /api/players/{playerID}/height")

    # Update player height
    cursor = cnx.cursor()
    query = f"UPDATE players Set height = height +1 WHERE playerID='{playerID}';"
    app.logger.info(f"Querying database: {query}")
    cursor.execute(query)
    cursor.close()
    response = ("Success", 200)
    app.logger.info(f"Returning response: {response}")
    return jsonify(response)


@app.route('/api/players', methods=["GET"])
def get_players():
    """ This API route returns all players in the players table """
    app.logger.info(f"GET /api/players")

    # Get all players
    cursor = cnx.cursor()
    query = f"SELECT * FROM players;"
    app.logger.info(f"Querying database: {query}")
    cursor.execute(query)

    players = []
    for player in cursor:
        player_json = {
            "playerId": player[0],
            "birthYear": player[1],
            "birthMonth": player[2],
            "birthDay": player[3],
            "birthCountry": player[4],
            "birthState": player[5],
            "birthCity": player[6],
            "deathYear": player[7],
            "deathMonth": player[8],
            "deathDay": player[9],
            "deathCountry": player[10],
            "deathState": player[11],
            "deathCity": player[12],
            "nameFirst": player[13],
            "nameLast": player[14],
            "nameGiven": player[15],
            "weight": player[16],
            "height": player[17],
            "bats": player[18],
            "throws": player[19],
            "debut": player[20],
            "finalGame": player[21],
            "retroID": player[22],
            "bbrefID": player[23]
        }
        players.append(player_json)

    cursor.close()
    response = {'players': players}
    app.logger.info(f"Returning response: {response}")
    return jsonify(response)


@app.route('/api/players/<playerID>', methods=["GET"])
def get_player(playerID):
    """ This API route returns a player by playerID """
    app.logger.info(f"GET /api/players/{playerID}")

    # Get player by playerID
    cursor = cnx.cursor()
    query = f"SELECT * FROM players WHERE playerID='{playerID}';"
    app.logger.info(f"Querying database: {query}")
    cursor.execute(query)

    players = []
    for player in cursor:
        player_json = {
            "playerId": player[0],
            "birthYear": player[1],
            "birthMonth": player[2],
            "birthDay": player[3],
            "birthCountry": player[4],
            "birthState": player[5],
            "birthCity": player[6],
            "deathYear": player[7],
            "deathMonth": player[8],
            "deathDay": player[9],
            "deathCountry": player[10],
            "deathState": player[11],
            "deathCity": player[12],
            "nameFirst": player[13],
            "nameLast": player[14],
            "nameGiven": player[15],
            "weight": player[16],
            "height": player[17],
            "bats": player[18],
            "throws": player[19],
            "debut": player[20],
            "finalGame": player[21],
            "retroID": player[22],
            "bbrefID": player[23]
        }
        players.append(player_json)

    cursor.close()
    response = {'players': players}

    app.logger.info(f"Returning response: {response}")
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)

