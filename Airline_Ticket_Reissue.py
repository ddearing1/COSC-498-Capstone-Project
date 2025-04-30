import mysql.connector  # Import the mysql.connector module

try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="2329Amina$",  # Replace with your MySQL password
    )
    print("Connected to the MySQL server successfully!")

    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # Execute the SQL command to show grants for 'ddearing1'
    cursor.execute("SHOW GRANTS FOR 'ddearing1'@'localhost';")

    # Fetch and print the results
    results = cursor.fetchall()
    print("Grants for 'ddearing1':")
    for row in results:
        print(row)

    # Close the connection
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")



