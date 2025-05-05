import pytest
import mysql.connector

@pytest.fixture(scope="module")
def db_connection():
    print("Attempting to connect to the database...")
    connection = mysql.connector.connect(
        host="localhost",
        user="ddearing1",
        password="2329Amina$",
        database="final_airline_reissue"  # Correct database name
    )
    print("Connection successful!")
    yield connection
    connection.close()

@pytest.fixture(scope="module", autouse=True)
def create_test_tables(db_connection):
    cursor = db_connection.cursor()

    # Create tables if they do not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Passengers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            column1 VARCHAR(255),
            column2 VARCHAR(255)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Flights (
            id INT AUTO_INCREMENT PRIMARY KEY,
            column1 VARCHAR(255),
            column2 VARCHAR(255)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Reservations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            column1 VARCHAR(255),
            column2 VARCHAR(255)
        );
    """)

    db_connection.commit()
    cursor.close()

@pytest.fixture(scope="function")
def setup_test_data(db_connection):
    cursor = db_connection.cursor()
    
    # Set up test data in Passengers table
    cursor.execute("INSERT INTO Passengers (column1, column2) VALUES ('value1', 'value2');")
    # Set up test data in Flights table
    cursor.execute("INSERT INTO Flights (column1, column2) VALUES ('value3', 'value4');")
    # Set up test data in Reservations table
    cursor.execute("INSERT INTO Reservations (column1, column2) VALUES ('value5', 'value6');")
    
    db_connection.commit()
    yield
    
    # Clean up test data from all tables
    cursor.execute("DELETE FROM Passengers;")
    cursor.execute("DELETE FROM Flights;")
    cursor.execute("DELETE FROM Reservations;")
    
    db_connection.commit()
    cursor.close()

def test_passengers_table(db_connection, setup_test_data):
    cursor = db_connection.cursor()
    # Select data from Passengers table
    cursor.execute("SELECT * FROM Passengers;")
    result = cursor.fetchall()
    assert len(result) == 1  # Ensure exactly 1 row was inserted
    cursor.close()

def test_flights_table(db_connection, setup_test_data):
    cursor = db_connection.cursor()
    # Select data from Flights table
    cursor.execute("SELECT * FROM Flights;")
    result = cursor.fetchall()
    assert len(result) == 1  # Ensure exactly 1 row was inserted
    cursor.close()

def test_reservations_table(db_connection, setup_test_data):
    cursor = db_connection.cursor()
    # Select data from Reservations table
    cursor.execute("SELECT * FROM Reservations;")
    result = cursor.fetchall()
    assert len(result) == 1  # Ensure exactly 1 row was inserted
    cursor.close()

def test_database_operations(db_connection):
    cursor = db_connection.cursor()
    # Show databases
    cursor.execute("SHOW DATABASES;")
    result = cursor.fetchall()
    for db in result:
        print(db)
    cursor.close()
