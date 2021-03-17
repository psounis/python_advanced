from dbtools import *

connector = open_connection()

try:
    mod = 2
    if mod == 1: # store to db
        insert_with_blob(connector, "bs.png", "beautiful soup logo")
        connector.commit()
        insert_with_blob(connector, "mysql.png", "mysql logo")
        connector.commit()
    else: # read from db
        res = read_blob(connector,1)
        with open("copy.png", "wb") as f:
            f.write(res)

except MYSQL.Error as e:
    print(e)

close_connection(connector)
