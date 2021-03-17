from dbtools import *

connector = open_connection()

try:
    results = call_stored(connector, 'country_cities', ['Greece'])

    for result in results:
        print(result)

except MYSQL.Error as e:
    print(e)

close_connection(connector)
