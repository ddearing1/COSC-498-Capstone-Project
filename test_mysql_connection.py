import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='ddearing1',  # Replace with your MySQL username
    password='2329Amina$',  # Replace with your MySQL password
    database='airline_reissues'  # Use the test database for testing
)

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Print a success message
print("Connected to the database successfully!")

# Show databases
cursor.execute("SHOW DATABASES;")
for db in cursor:
    print(db)

# Close the connection
cursor.close()
connection.close()