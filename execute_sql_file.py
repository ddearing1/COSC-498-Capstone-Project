import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="ddearing1",
    password="2329Amina$",
    database="final_airline_reissue"
)

cursor = connection.cursor()

# Read the SQL file
with open("/Users/donnadearing/Desktop/COSC-498-Capstone-Project/final_airline_reissue.sql", "r") as file:
    sql_script = file.read()

# Execute the SQL script
for statement in sql_script.split(";"):
    if statement.strip():  # Skip empty statements
        cursor.execute(statement)

connection.commit()
print("SQL script executed successfully!")

# Close the connection
cursor.close()
connection.close()