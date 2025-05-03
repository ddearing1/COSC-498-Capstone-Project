# Read the SQL file
with open("/Users/donnadearing/Desktop/COSC-498-Capstone-Project/final_airline_reissue.sql", "r") as file:
    sql_script = file.read()

# List of column names to search for
columns_to_check = ["passenger_id", "flight_number", "ticket_status", "origin_city"]

# Check if each column exists in the script
for column in columns_to_check:
    if column in sql_script:
        print(f"Column '{column}' found in the script.")
    else:
        print(f"Column '{column}' NOT found in the script.")