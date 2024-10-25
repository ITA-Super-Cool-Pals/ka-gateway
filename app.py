
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Routes for Rooms Service
@app.route('/rooms')
def get_rooms():
    room_url = f'http://ka-rooms:5001'
    response = requests.get(room_url)
    return jsonify(response.json())

app.run(host='0.0.0.0')
