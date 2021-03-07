from dbtools import *

connector = open_connection()

try:
    cursor = connector.cursor(dictionary=True)

    query = "SELECT * FROM country"
    cursor.execute(query)

    country = cursor.fetchone()
    while country is not None:
        print(f"{country['Name']}({country['Continent']}). Next? Press Enter...", end="")
        input()
        country = cursor.fetchone()

except MYSQL.Error as e:
    print(e)

close_connection(connector)
