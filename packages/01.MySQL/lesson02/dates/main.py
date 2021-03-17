from dbtools import *
from datetime import *

connector = open_connection()

try:
    query = "SELECT * FROM dates"
    results = query_full_results(connector, query)

    vdate = results[0]["vdate"]
    print("A date: " + vdate.strftime("%d.%m.%Y"))

    td = results[0]["vtime"]
    vtime = time(td.seconds//3600, (td.seconds%3600)//60, td.seconds%60)
    print("A time: " + str(vtime))

    vdatetime = results[0]["vdatetime"]
    print("A datetime: " + vdatetime.strftime("%d.%m.%Y %H:%M:%S"))

    vtimestamp = results[0]["vtimestamp"]
    print("A timestamp: " + vtimestamp.strftime("%d.%m.%Y %H:%M:%S"))

    query = "INSERT INTO dates(vdate, vtime, vdatetime) VALUES (%s, %s, %s)"
    tuple_values = (datetime.now().date(), datetime.now().time(), datetime.now())
    insert_with_tuple(connector, query, tuple_values)
    connector.commit()

except MYSQL.Error as e:
    print(e)

close_connection(connector)
