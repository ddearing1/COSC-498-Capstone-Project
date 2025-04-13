INSERT INTO Reservations (passenger_id, flight_id, ticket_status)
VALUES
(1, 'AA171', 'booked'),
(2, 'AA348', 'reissued'),
(3, 'AA2550', 'canceled');

INSERT INTO Flights (date_of_flight, departure_time, origin_city, arrival_time, 
destination_city)
VALUES
(2025-04-15, '07:00:00', 'New York JFK', '10:20:00' 'Los Angeles'),
(2025-04-16, '21:00:00', 'Dallas Fort Worth', '22:27' 'Santa Ana'),
(2025-04-22', '18:10:00', 'Knoxville', '19:50:00' 'Dallas Fort Worth');

INSERT INTO Passengers TABLE (record_locator, passenger_id, name)
VALUES
(QHQGVB, '1', 'Chester Drawers'),
(EOAGKF, '2', 'Snap Crackle Pop'),
(MZUSQY, '3', 'Bud Weiser')