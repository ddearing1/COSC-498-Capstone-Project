DESCRIBE passengers;
DESCRIBE flights;
DESCRIBE reservations;



INSERT INTO flights (passenger_id, flight_id, date_of_flight, departure_time, origin_city, arrival_time, destination_city)
VALUES
(1, 'AA2469', '2025-04-15', '07:00:00', 'New York JFK', '10:20:00' 'Los Angeles'),
(2, 'AA890', '2025-04-16', '14:00:00', 'Chicago', '17:00:00', 'Miami');
(3, 'AA348', '2025-04-16', '21:00:00', 'Dallas Fort Worth', '22:27', 'Santa Ana');
(4, 'AA36', '2025-04-22', '18:10:00', 'Dallas Fort Worth', '13:50:00', 'Madrid');

@app.route('/create_reservation', methods=['POST'])
def create_reservation():
    data = request.json  # Expecting JSON input
    passenger_id = data['passenger_id']
    flight_id = data['flight_number']
    date_of_flight = data['departure_date']
    departure_time = data['departure_time']
    origin_city = data['origin']
    arrival_time = data['arrival_time']
    destination_city = data['destination']

    # Insert into the database
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO reservations (passenger_id, flight_number, departure_date, departure_time, arrival_time, origin, destination)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (passenger_id, flight_id, date_of_flight, departure_time, origin_city, arrival_time, destination_city))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Reservation created successfully!"})