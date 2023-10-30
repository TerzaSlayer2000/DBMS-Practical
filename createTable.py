import mysql.connector
# Connect to the MySQL server
conn = mysql.connector.connect(host='localhost', user='root', password='root', database='sain')
mycursor = conn.cursor()

# Define the SQL query to create the table

create_table_query = """
  CREATE TABLE IF NOT EXISTS examResults (
    resultId INT PRIMARY KEY,
    studentId INT,
    examId INT,
    score DECIMAL(5, 2),
    FOREIGN KEY (studentId) REFERENCES student(studentId),
    FOREIGN KEY (examId) REFERENCES exam(examId)
)
"""

# Execute the SQL query
mycursor.execute(create_table_query)
# Commit the changes
conn.commit()
# Close the connection
conn.close()
