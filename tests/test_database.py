import unittest
import mysql.connector

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = mysql.connector.connect(
            host='localhost',
            user='ddearing1',
            password='2329Amina$',
            database='Final'
        )
        cls.cursor = cls.connection.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.connection.close()

    def test_connection(self):
        self.assertIsNotNone(self.connection)

    def test_database_operations(self):
        self.cursor.execute("SELECT DATABASE();")
        current_database = self.cursor.fetchone()
        self.assertEqual(current_database[0], 'Final')

if __name__ == '__main__':
    unittest.main()