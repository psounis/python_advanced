import mysql.connector
from connect import open_connection, close_connection
MYSQL = mysql.connector


def print_country(country):
    print("="*35)
    print(f"Code: {country[0]}")
    print(f"Name: {country[1]}")
    print(f"Continent: {country[2]}")
    print(f"Region: {country[3]}")
    print(f"Surface Area: {country[4]}")
    print(f"Independence Year: {country[5]}")
    print(f"Population: {country[6]}")
    print(f"Life Expectancy: {country[7]}")
    print(f"GNP: {country[8]}")
    print(f"GNPold: {country[9]}")
    print(f"Local Name: {country[10]}")
    print(f"Government Form: {country[11]}")
    print(f"Head of State: {country[12]}")
    print(f"Capital: {country[13]}")
    print(f"Code2: {country[14]}")


connector = open_connection()

try:
    cursor = connector.cursor()

    query = "SELECT * FROM country"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print_country(row)

    cursor.close()
except MYSQL.Error as e:
    print(e)

close_connection(connector)
