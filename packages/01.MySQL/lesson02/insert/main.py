from dbtools import *

connector = open_connection()

try:
    query = """INSERT INTO city (Name, countryCode, District, Population)
                    VALUES('Chania','GRC', 'Crete', 100000)"""

    id = insert_query(connector,query)

    print("Row inserted with id: " + str(id))

    connector.commit()

except MYSQL.Error as e:
    print(e)

close_connection(connector)
