from collections import namedtuple
import mysql.connector
from connect import open_connection, close_connection
MYSQL = mysql.connector

conn = open_connection()

try:
    cursor = conn.cursor()

    query = "SELECT Code, Name, Population FROM country"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)

    Country = namedtuple("Country", "Code Name Population")
    c = Country(*rows[0])
    print(c.Code, c.Name, c.Population)


    cursor.close()
except MYSQL.Error as e:
    print(e)

close_connection(conn)
