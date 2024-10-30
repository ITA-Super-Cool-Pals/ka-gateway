
from flask import Flask, jsonify, request
import requests, app_csv_convert

app = Flask(__name__)

# Routes for Rooms Service
@app.route('/rooms')
def get_rooms():
    room_url = 'http://ka-rooms:5000/rooms'
    response = requests.get(room_url)
    return jsonify(response.json())

# Routes for rooms data as csv
@app.route('/rooms/csv')
def get_rooms_csv():
    room_url = 'http://ka-rooms:5000/rooms'
    response = requests.get(room_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="rooms.csv")

# Bar Sales route
@app.route('/barsales')
def get_bar_sales():
    bar_sales_url = 'http://ka-bar-sales:5000/barsales'
    response = requests.get(bar_sales_url)
    return jsonify(response.json())

# Bar sales data as csv
@app.route('/barsales/csv')
def get_bar_sales_csv():
    bar_sales_url = 'http://ka-bar-sales:5000/barsales'
    response = requests.get(bar_sales_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="bar_sales.csv")


app.run(host='0.0.0.0')
