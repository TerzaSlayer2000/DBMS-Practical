import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='root', database='sain')
mycursor = conn.cursor()

# Define the SQL query to select all rows from the student table
select_query = "SELECT * FROM examresults;"

# Execute the SQL query
mycursor.execute(select_query)

# Fetch all the rows
result = mycursor.fetchall()

# Display the results in the console
for row in result:
    print(row)

# Close the connection
conn.close()
