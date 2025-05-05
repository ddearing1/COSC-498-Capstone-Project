import unittest
import mysql.connector

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            print("Attempting to connect to the database...")
            cls.connection = mysql.connector.connect(
                host='localhost',
                user='ddearing1',
                password='2329Amina$',
                database='final_airline_reissue'  # Correct database name
            )
            print("Connection successful!")
            cls.cursor = cls.connection.cursor()
            print("Connected to database:", cls.connection.is_connected())
            
            # Grant privileges and flush
            cls.cursor.execute("GRANT ALL PRIVILEGES ON final_airline_reissue.* TO 'ddearing1'@'localhost';")
            cls.cursor.execute("FLUSH PRIVILEGES;")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.connection.close()

    def test_connection(self):
        self.assertIsNotNone(self.connection)

    def test_database_operations(self):
        self.cursor.execute("SELECT DATABASE();")
        current_database = self.cursor.fetchone()
        print("Current database:", current_database)
        self.assertEqual(current_database[0], 'final_airline_reissue')

if __name__ == '__main__':
    unittest.main()
