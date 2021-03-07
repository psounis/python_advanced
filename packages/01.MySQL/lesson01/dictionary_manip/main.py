import mysql.connector
from connect import open_connection, close_connection
MYSQL = mysql.connector


connector = open_connection()

try:
    cursor = connector.cursor(dictionary=True)

    query = "SELECT * FROM country"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(f"{row['Name']}({row['Continent']})")

except MYSQL.Error as e:
    print(e)

close_connection(connector)
