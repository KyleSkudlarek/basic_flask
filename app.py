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
logging.basicConfig(filename=os.path.join(app.root_path, 'logs', 'app.log'), level=logging.INFO, force=True)



@app.route('/player/', methods=["POST"])
def add_player():

    # Get player data from request payload
    payload = request.get_json(force=True)
    app.logger.info(payload)
    name = payload.get('name')
    score = payload.get('score')

    # Insert into database
    cursor = cnx.cursor()
    query = f"INSERT INTO players (name, score) VALUES ('{name}', '{score}');"
    app.logger.info(query)
    cursor.execute(query)
    cursor.close()
    return "Success", 200


@app.route('/player/<name>', methods=["GET"])
def get_player(name):
    # Query from database
    cursor = cnx.cursor()
    query = f"SELECT * FROM players WHERE Name='{name}';"
    app.logger.info(query)
    cursor.execute(query)

    names = []
    for name in cursor:
        app.logger.info(f"name: {name}")
        names.append(name)

    cursor.close()
    my_dict = {"names": names}
    return jsonify(my_dict)


if __name__ == "__main__":
    app.run(debug=True)

