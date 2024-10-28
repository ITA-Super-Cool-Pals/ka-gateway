
from flask import Flask, jsonify, request
import requests, app_csv_convert

app = Flask(__name__)

# Routes for Rooms Service
@app.route('/rooms')
def get_rooms():
    room_url = f'http://ka-rooms:5000/rooms'
    response = requests.get(room_url)
    return jsonify(response.json())

# Routes for rooms data as csv
@app.route('/rooms/csv')
def get_rooms_csv():
    room_url = f'http://ka-rooms:5000/rooms'
    response = requests.get(room_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="rooms.csv")


app.run(host='0.0.0.0')
