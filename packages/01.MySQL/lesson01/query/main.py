import mysql.connector
from connect import open_connection, close_connection
MYSQL = mysql.connector

conn = open_connection()

try:
    cursor = conn.cursor()

    query = "SELECT * FROM country"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()
except MYSQL.Error as e:
    print(e)

close_connection(conn)
