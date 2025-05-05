import os
import mysql.connector

class TestDatabase:
    @classmethod
    def setUpClass(cls):
        cls.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "testdb")
        )
        print("Database connection successful!")