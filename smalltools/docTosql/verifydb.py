import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='study_db'
)

# Execute the query
cursor = connection.cursor()
cursor.execute("DESCRIBE YourData")

# Fetch and print the results
for column in cursor.fetchall():
    print(column)

# Close the connection
cursor.close()
connection.close()