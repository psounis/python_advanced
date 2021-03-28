from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+mysqlconnector://pythonuser:pwd1234@localhost/pyworld')
metadata = MetaData()

city = Table('city', metadata, autoload=True, autoload_with=engine)

conn = engine.connect()

query = city.select().limit(5)
print("datatype: ", type(query))
print("full query: ", query)

result_set = conn.execute(query)
print("result set: ", result_set)

for row in result_set:
    print(row)
    print(row[0], row[1])
    print(row["ID"], row["Name"])
    print(row.ID, row.Name)
    print(row[city.c.ID], row[city.c.Name])

