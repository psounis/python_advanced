from dbtools import *

connector = open_connection()


iter_query = query_iter_many(connector, 10, "SELECT * FROM country LIMIT 42")

for countries in iter_query:
    for country in countries:
        print(f"{country['Name']}({country['Continent']}). ")
    print("="*10 + ". Next? Press Enter...", end="")
    input()


close_connection(connector)
