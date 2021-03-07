from dbtools import *

connector = open_connection()

try:
    cursor = connector.cursor(dictionary=True)

    query = "SELECT * FROM country LIMIT 42"
    cursor.execute(query)

    countries = cursor.fetchmany(10)
    while countries:
        for country in countries:
            print(f"{country['Name']}({country['Continent']}). ")
        print("="*10 + ". Next? Press Enter...", end="")
        input()
        countries = cursor.fetchmany(10)

except MYSQL.Error as e:
    print(e)

close_connection(connector)
