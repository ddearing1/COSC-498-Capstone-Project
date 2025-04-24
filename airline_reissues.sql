CREATE TABLE Passengers (
    passenger_id INT AUTO_INCREMENT PRIMARY KEY,
    record_locator VARCHAR(10),
    name VARCHAR(255)
);

CREATE TABLE Flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(10),
    date_of_flight DATE,
    departure_time TIME,
    arrival_time TIME,
    class_of_service VARCHAR(50),
    origin_city VARCHAR(255),
    destination_city VARCHAR(255)
);

CREATE TABLE Reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id INT,
    flight_id INT,
    ticket_status ENUM('booked', 'reissued', 'canceled'),
    FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES Flights(flight_id)
);

ALTER TABLE Reservations DROP PRIMARY KEY;
ALTER TABLE Reservations CHANGE COLUMN reservation_id record_locator INT AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE Reservations DROP PRIMARY KEY;
ALTER TABLE Reservations CHANGE COLUMN reservation_id record_locator INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE Reservations CHANGE COLUMN reservation_id record_locator INT AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE Flights MODIFY COLUMN flight_id VARCHAR(6);

DELIMITER //

CREATE TRIGGER validate_flight_id
BEFORE INSERT ON Flights
FOR EACH ROW
BEGIN
    IF NEW.flight_id NOT REGEXP '^[A-Z]{2}[0-9]{1,4}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid flight_id format';
    END IF;
END//

DELIMITER ;

SHOW DATABASES;


