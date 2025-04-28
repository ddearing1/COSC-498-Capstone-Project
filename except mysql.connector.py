import mysql.connector

try:
    # Connect to the MySQL server as root
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Use the root user to modify other users
        password="your_root_password"  # Replace with your root password
    )
    print("Connected to the MySQL server successfully!")

    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # Execute the SQL command to update the password for 'ddearing1'
    cursor.execute("ALTER USER 'ddearing1'@'localhost' IDENTIFIED BY '2329Amina$';")
    cursor.execute("FLUSH PRIVILEGES;")
    print("Password for 'ddearing1' updated successfully!")

    # Close the connection
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")

