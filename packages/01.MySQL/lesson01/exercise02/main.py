import mysql.connector
from connect import open_connection, close_connection
MYSQL = mysql.connector


connector = open_connection()

try:
    cursor = connector.cursor(dictionary=True)

    query_cnt = "SELECT name, code FROM country WHERE continent='North America'"
    cursor.execute(query_cnt)

    rows_countries = cursor.fetchall()

    for row_country in rows_countries:
        cursor_city = connector.cursor(dictionary=True)
        query_cit = "SELECT name FROM city WHERE countryCode='" + row_country["code"] + "'"
        cursor_city.execute(query_cit)
        row_cities = cursor_city.fetchall()
        print(row_country["name"] + "(" + ", ".join([cityd["name"] for cityd in row_cities]) + ")")
        cursor_city.close()

    cursor.close()
except MYSQL.Error as e:
    print(e)

close_connection(connector)
