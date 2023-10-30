import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='root')
mycursor=conn.cursor()
mycursor.execute("create database if not exists sain")
conn.close()