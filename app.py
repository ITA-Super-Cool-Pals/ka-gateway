
from flask import Flask, jsonify, request
import requests, app_csv_convert

app = Flask(__name__)

# Room service routes
@app.route('/rooms')
def get_rooms():
    room_url = 'http://ka-rooms:5000/rooms'
    response = requests.get(room_url)
    return jsonify(response.json())

@app.route('/rooms/csv')
def get_rooms_csv():
    room_url = 'http://ka-rooms:5000/rooms'
    response = requests.get(room_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="rooms.csv")

# Reviews routes
@app.route('/reviews')
def get_reviews():
    review_url = 'http://ka-reviews:5000/reviews'
    response = requests.get(review_url)
    return jsonify(response.json())

@app.route('/reviews/<int:id>')
def get_reviews_single(id):
    review_url = f'http://ka-reviews:5000/{id}'
    response = requests.get(review_url)
    return jsonify(response.json())

@app.route('/reviews', methods=['POST'])
def create_review():
    review_url = 'http://ka-reviews:5000'
    review_data = request.get_json()
    response = requests.get(url = review_url, json = review_data)
    return jsonify(response.json())

@app.route('/reviews/csv')
def get_reviews_csv():
    review_url = 'http://ka-reviews:5000/reviews'
    response = requests.get(review_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="reviews.csv")

# Occupancy routes
@app.route('/occupancy')
def get_occupancy():
    occupancy_url = 'http://ka-occupancy:5000/occupancy'
    response = requests.get(occupancy_url)
    return jsonify(response.json())

@app.route('/occupancy/csv')
def get_occupancy_csv():
    occupancy_url = 'http://ka-occupancy:5000/occupancy'
    response = requests.get(occupancy_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="occupancy.csv")

# Bar sales routes
@app.route('/barsales')
def get_bar_sales():
    bar_sales_url = 'http://ka-bar-sales:5000/barsales'
    response = requests.get(bar_sales_url)
    return jsonify(response.json())

@app.route('/barsales/csv')
def get_bar_sales_csv():
    bar_sales_url = 'http://ka-bar-sales:5000/barsales'
    response = requests.get(bar_sales_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="bar_sales.csv")


app.run(host='0.0.0.0')
