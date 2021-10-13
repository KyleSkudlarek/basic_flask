from flask import Flask, request, jsonify
import mysql.connector

cnx = mysql.connector.connect(user='kyle', password='KJSkud26',
                              host='127.0.0.1',
                              database='main',
                              port=3306)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my first API call!'


@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True)
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)


@app.route('/get', methods=["GET"])
def testget():
     cursor = cnx.cursor()

     query = ("select * from mydata;")

     cursor.execute(query)

     names = []
     for name in cursor:
          print(f"name: {name}")
          names.append(name)

     cursor.close()

     my_dict = {"names": names}


     return jsonify(my_dict)