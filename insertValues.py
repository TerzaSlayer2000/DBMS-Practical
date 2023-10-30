import mysql.connector
# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='root', database='sain')
mycursor = conn.cursor()

# Define the SQL query to create the table

create_table_query = """

 INSERT INTO examresults (resultId, studentId, examId, score)
 VALUES (501, 1, 201, 92.5),
        (502, 2, 201, 88.0),
        (503, 3, 202, 95.5),
        (504, 4, 203, 89.0),
        (505, 5, 204, 94.5),
        (506, 6, 205, 91.0),
        (507, 7, 201, 87.5);
"""

# Execute the SQL query
mycursor.execute(create_table_query)
# Commit the changes
conn.commit()
# Close the connection
conn.close()



