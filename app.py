
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
    review_url = f'http://ka-reviews:5000/reviews/{id}'
    response = requests.get(review_url)
    return jsonify(response.json())

@app.route('/reviews', methods=['POST'])
def create_review():
    review_url = 'http://ka-reviews:5000/reviews'
    review_data = request.get_json()

    # Send POST request to ka-reviews service
    review_response = requests.post(url=review_url, json=review_data)

    # Check status code of the response from ka-reviews
    if review_response.status_code == 201:
        return jsonify(review_response.json()), 201
    elif review_response.status_code == 500:
        return jsonify({"error": "server error"}), 500
    else:
        return jsonify(review_response.json()), review_response.status_code

@app.route('/reviews/csv')
def get_reviews_csv():
    review_url = 'http://ka-reviews:5000/reviews'
    response = requests.get(review_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="reviews.csv")


# Booking routes
@app.route('/bookings')
def get_bookings():
    bookings_url = 'http://ka-bookings:5000/bookings'
    response = requests.get(bookings_url)
    return jsonify(response.json())

@app.route('/bookings/<int:id>')
def get_bookings_single(id):
    bookings_url = f'http://ka-bookings:5000/bookings/{id}'
    response = requests.get(bookings_url)
    return jsonify(response.json())

@app.route('/bookings', methods=['POST'])
def create_booking():
    bookings_url = 'http://ka-bookings:5000/create'
    bookings_data = request.get_json()

    # Send POST request to ka-bookings service
    bookings_response = requests.post(url=bookings_url, json=bookings_data)

    # Check status code of response from ka-bookings
    if bookings_response.status_code == 201:
        return jsonify(bookings_response.json()), 201
    elif bookings_response.status_code == 500:
        return jsonify({"error": "server error"}), 500
    else:
        return jsonify(bookings_response.json()), bookings_response.status_code

@app.route('/bookings/csv')
def get_bookings_csv():
    bookings_url = 'http://ka-bookings:5000/bookings'
    response = requests.get(bookings_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="bookings.csv")


# Guest routes
@app.route('/guests')
def get_guests():
    guests_url = 'http://ka-guests:5000/guests'
    response = requests.get(guests_url)
    return jsonify(response.json())

@app.route('/guests/<int:id>')
def get_guests_single(id):
    guests_url = f'http://ka-guests:5000/guests/{id}'
    response = requests.get(guests_url)
    return jsonify(response.json())

@app.route('/guests', methods=['POST'])
def create_guest():
    guests_url = 'http://ka-guests:5000/guests'
    guests_data = request.get_json()

    # Send POST request to ka-guests service
    guests_response = requests.post(url=guests_url, json=guests_data)

    # Check status code of response from ka-guests
    if guests_response.status_code == 201:
        return jsonify(guests_response.json()), 201
    elif guests_response.status_code == 500:
        return jsonify({"error": "server error"}), 500
    else:
        return jsonify(guests_response.json()), guests_response.status_code

@app.route('/guests/csv')
def get_guests_csv():
    guests_url = 'http://ka-guests:5000/guests'
    response = requests.get(guests_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="guests.csv")


# Occupancy routes
@app.route('/occupancy')
def get_occupancy():
    occupancy_url = 'http://ka-occupancy:5000/occupancy/rooms'
    response = requests.get(occupancy_url)
    return jsonify(response.json())

@app.route('/occupancy/csv')
def get_occupancy_csv():
    occupancy_url = 'http://ka-occupancy:5000/occupancy/rooms'
    response = requests.get(occupancy_url)
    json_data = response.json()
    return app_csv_convert.convert_json_to_csv(json_data, filename="occupancy.csv")

@app.route('/occupancy', methods=['POST'])
def create_occupancy():
    occupancy_url = 'http://ka-occupancy:5000/occupancy'
    occupancy_data = request.get_json()

    # Send POST request to ka-occupancy service
    occupancy_response = requests.post(url=occupancy_url, json=occupancy_data)

    # Check status code of response from ka-occupancy
    if occupancy_response.status_code == 201:
        return jsonify(occupancy_response.json()), 201
    elif occupancy_response.status_code == 500:
        return jsonify({"error": "server error"}), 500
    else:
        return jsonify(occupancy_response.json()), occupancy_response.status_code

@app.route('/occupancy/<int:id>', methods=['PATCH'])
def update_occupancy(id):
    occupancy_url = f'http://ka-occupancy:5000/occupancy/{id}'
    occupancy_data = request.get_json()

    # Send PATCH request to ka-occupancy service
    occupancy_response = requests.patch(url=occupancy_url, json=occupancy_data)

    # Check status code of response from ka-occupancy
    if occupancy_response.status_code == 200:
        return jsonify(occupancy_response.json()), 200
    elif occupancy_response.status_code == 500:
        return jsonify({"error": "server error"}), 500
    else:
        return jsonify(occupancy_response.json()), occupancy_response.status_code



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
