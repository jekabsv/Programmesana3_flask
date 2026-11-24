from flask import Flask, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

@app.route('/sensor/data', methods=['POST'])
def receive_sensor_data():
    mydb = mysql.connector.connect(
        host="database",
        user="root",
        password="root",
        database="jacobsDB",
        port=3306
    )
    mycursor = mydb.cursor()

    data = request.get_json()
    json_string = json.dumps(data)
    
    sql = "INSERT INTO _data (__data) VALUES (%s)"
    mycursor.execute(sql, (json_string,))
    mydb.commit()
    
    mycursor.close()
    mydb.close()
    
    print(data)

    return jsonify({
        "status": "success",
        "received": data
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
