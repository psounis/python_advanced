from dbtools import *

connector = open_connection()


iter_query = query_iter_one(connector, "SELECT * FROM country")

for item in iter_query:
    print(f"{item['Name']}({item['Continent']}). Next? Press Enter...", end="")
    input()


close_connection(connector)
