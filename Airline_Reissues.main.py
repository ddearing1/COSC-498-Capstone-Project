import mysql.connector  # Import the mysql.connector module

try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="ddearing1",  # Replace with your MySQL username
        password="2329Amina$",  # Replace with your MySQL password
        database="airline_reissues"  # Replace with your database name
    )
    print("Connected to the database successfully!")

    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # Execute the SQL command to show databases
    cursor.execute("SHOW DATABASES;")
    for db in cursor:
        print(db)

    # Close the connection
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")















