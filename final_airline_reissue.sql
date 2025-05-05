-- STEP 1: Create database
CREATE DATABASE final_airline_reissue;

USE final_airline_reissue;

-- STEP 2: Drop tables if they exist
DROP TABLE IF EXISTS Reservations;
CREATE TABLE Passengers (
   passenger_id INT AUTO_INCREMENT PRIMARY KEY,
   record_locator VARCHAR(10),
   name VARCHAR(255)
);

-- STEP 4: Create Flights table
CREATE TABLE Flights (
   flight_id INT AUTO_INCREMENT PRIMARY KEY,
   flight_number VARCHAR(10),
   date_of_flight DATE,
   departure_time TIME,
   arrival_time TIME,
   class_of_service VARCHAR(50),
   origin_city VARCHAR(255),
   destination_city VARCHAR(255),
   CONSTRAINT flight_number_format CHECK (flight_number REGEXP '^[A-Z]{2}[0-9]{1,4}$')
);

-- STEP 5: Create Reservations table
CREATE TABLE Reservations (
   reservation_id INT AUTO_INCREMENT PRIMARY KEY,
   passenger_id INT,
   flight_id INT,
   ticket_status ENUM('booked', 'reissued', 'canceled'),
   FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id),
   FOREIGN KEY (flight_id) REFERENCES Flights(flight_id)
);

-- STEP 6: Insert sample passengers
INSERT INTO Passengers (record_locator, name)
VALUES
('QHQGVB', 'Chester Drawers'),
('EOAGKF', 'Snap Crackle Pop'),
('MZUSQY', 'Bud Weiser');

-- STEP 7: Insert sample flights
INSERT INTO Flights (flight_number, date_of_flight, departure_time, arrival_time, class_of_service, origin_city, destination_city)
VALUES
('AA2469', '2025-04-15', '07:00:00', '10:20:00', 'Economy', 'New York JFK', 'Los Angeles'),
('AA890',  '2025-04-16', '14:00:00', '17:00:00', 'Economy', 'Chicago', 'Miami'),
('AA348',  '2025-04-16', '21:00:00', '22:27:00', 'Economy', 'Dallas Fort Worth', 'Santa Ana'),
('AA36',   '2025-04-22', '18:10:00', '13:50:00', 'Business', 'Dallas Fort Worth', 'Madrid');

-- You can run this SELECT manually in your SQL editor to get actual flight_id values:
-- SELECT flight_id, flight_number FROM Flights;

-- STEP 9: Insert reservations (assuming flight_ids are 1 to 4)
INSERT INTO Reservations (passenger_id, flight_id, ticket_status)
VALUES
(1, 1, 'booked'),
(2, 3, 'reissued'),
(3, 4, 'canceled');

-- STEP 10: Show databases
USE final_airline_reissue;
GRANT ALL PRIVILEGES ON final_airline_reissue.* TO 'ddearing1'@'localhost';
FLUSH PRIVILEGES;

SHOW DATABASES;
USE final_airline_reissue;
SHOW TABLES;

SOURCE /Users/donnadearing/Desktop/COSC-498-Capstone-Project/final_airline_reissue.sql;