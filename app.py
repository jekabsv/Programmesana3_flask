from flask import Flask, request, jsonify
import mysql.connector
import json

mydb = mysql.connector.connect(
  host="database",
  user="root",
  password="root",
  database="jacobsDB",
  port=3307
)

mycursor = mydb.cursor()

sql = "INSERT INTO _data (__data) VALUES (%s)"

app = Flask(__name__)

@app.route('/sensor/data', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    json_string = json.dumps(data)
    mycursor.execute(sql, (json_string,))
    mydb.commit()
    print(data)
