# ka-gateway
Gateway for the various of king arthur microservices

## Setup

1. Build the docker image:
```
docker build -t ka-gateway https://github.com/ITA-Super-Cool-Pals/ka-gateway.git#main
```

2. Run the docker image:
```
docker run --rm -d -p 5000:5000 --name ka-gatewya --network ka-network ka-gateway
```

## Alternative quick setup for all microservices

The following process will help quickly set up the needed docker network, build the images from latest repositories and run the containers.

1. Clone this repository:
```
git clone https://github.com/ITA-Super-Cool-Pals/ka-gateway.git
```

2. CD into the ka-gateway directory
```
cd ka-gateway
```

3. Run the `ka-docker-setup` script using bash:
```
bash ka-docker-setup
```

4. Follow the on screen prompts:
    - Create a network
    - Build the images
    - Run the containers

## API Endpoints

### Get list of rooms
- URL: `/rooms`
- Method: `GET`
- Response:
  - **200:** List rooms

### Get list of rooms in CSV format
- URL: `/rooms/csv`
- Method: `GET`
- Response:
  - **200:** List rooms as csv
---
### Get list of reviews
- URL: `/reviews`
- Method: `GET`
- Response:
  - **200:** List reviews

### Get list of reviews in CSV format
- URL: `/reviews/csv`
- Method: `GET`
- Response:
  - **200:** List reviews as csv

### Get single review by id
- URL: `/reviews/{id}`
- Method: `GET`
- Response:
  - **200:** List single review
  - **404:** review ID not found

### Post new review
- URL: `/reviews`
- Method: `POST`
- Request Body:
  ```
  {
    "RoomId": room_id (INT),
    "GuestId": guest_id (INT),
    "Review": "Review text" (STRING),
    "Rating": rating (DOUBLE)
  }
  ```
- Response:
  - **201:** Review created
  - **404:** Room or guest id not found
  - **400:** Guest already reviewed room
---
### Get list of bookings
- URL: `/bookings`
- Method: `GET`
- Response:
  - **200:** List bookings

### Get list of bookings in CSV format
- URL: `/bookings/csv`
- Method: `GET`
- Response:
  - **200:** List bookings as csv

### Get single booking by id
- URL: `/bookings/{id}`
- Method: `GET`
- Response:
  - **200:** List single bookings
  - **404:** booking not found

### Post new booking
- URL: `/bookings`
- Method: `POST`
- Request Body:
  ```
  {
    "bookingId": booking_id (INT),
    "roomId": room_id (INT),
    "guestId": guest_id (INT),
    "season": "season" (STRING),
    "nrOfDays": days (INT),
    "totalPrice": price (FLOAT)
  }
  ```
- Response:
  - **201:** Booking created
  - **400:** Missing required booking data
  - **500:** Failed to create booking or could not fetch room type
---
### Get list of guests
- URL: `/guests`
- Method: `GET`
- Response:
  - **200:** List Guests

### Get list of guests in CSV format
- URL: `/guests/csv`
- Method: `GET`
- Response:
  - **200:** List guests as csv

### Get single guest by id
- URL: `/guests/{id}`
- Method: `GET`
- Response:
  - **200:** List single guest
  - **404:** Guest not found

### Create new guest
- URL: `/guests`
- Method: `POST`
- Request Body:
  ```
  {
    "guestId": id (INT),
    "name": "Name" (STRING),
    "tlf": number (INT)
  }
  ```
- Response:
  - **201:** Guest created
  - **409:** Guest ID already in use
  - **400:** Missing required data
  - **500:** Error creating guest
---
### Get list of occupancy data
- URL: `/occupancy`
- Method: `GET`
- Response:
  - **200:** List occupancy data

### Get list of occupancy data in CSV format
- URL: `/occupancy/csv`
- Method: `GET`
- Response:
  - **200:** List occupancy data as csv
---
### Get list of bar sales data
- URL: `/barsales`
- Method: `GET`
- Response:
  - **200:** List bar sales data

### Get list of bar sales data in CSV format
- URL: `/barsales/csv`
- Method: `GET`
- Response:
  - **200:** List bar sales data as csv
