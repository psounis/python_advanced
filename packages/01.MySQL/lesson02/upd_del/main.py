from dbtools import *

connector = open_connection()

try:
    query = """UPDATE city
                    SET name='Χανιά'
                    WHERE name='Chania'"""

    update_query(connector, query)
    connector.commit()

    print("Check your db. Press Enter...")
    input("")

    query = """DELETE FROM city
                        WHERE name='Χανιά'"""

    delete_query(connector, query)
    connector.commit()


except MYSQL.Error as e:
    print(e)

close_connection(connector)
