import os
import mysql.connector
import pytest

class TestDatabase:
    def test_connection(self):
        # Test if the database connection is successful
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="ddearing1",
            password=os.getenv("MYSQL_PASSWORD"),
            database="airline_reissues"
        )
        assert connection.is_connected()
        connection.close()

    def setup_database_privileges(self):
        # Set up database privileges for the user
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="ddearing1",
            password=os.getenv("MYSQL_PASSWORD"),
            database="airline_reissues"
        )
        cursor = connection.cursor()
        cursor.execute("GRANT ALL PRIVILEGES ON airline_reissues.* TO 'ddearing1'@'localhost' IDENTIFIED BY '2329Amina$';")
        cursor.execute("FLUSH PRIVILEGES;")
        connection.close()

    def show_databases(self):
        # Show all databases
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="ddearing1",
            password=os.getenv("MYSQL_PASSWORD"),
            database="airline_reissues"
        )
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES;")
        for db in cursor:
            print(db[0])  # Print the database name
        connection.close()

# Configuration for MySQL client
client_config = {
    "user": "ddearing1",
    "password": "2329Amina$"
}