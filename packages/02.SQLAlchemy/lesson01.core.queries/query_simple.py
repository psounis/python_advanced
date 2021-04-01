from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+mysqlconnector://pythonuser:pwd1234@localhost/pyworld')
metadata = MetaData()

country = Table('country', metadata, autoload=True, autoload_with=engine)
city = Table('city', metadata, autoload=True, autoload_with=engine)
countrylanguage = Table('countrylanguage', metadata, autoload=True, autoload_with=engine)


conn = engine.connect()

# all
query = city.select()
print(query)

result = conn.execute(query)
for row in result:
    print(row)

input("Press Enter ")


# columns
query = select([city.c.ID, city.c.Name])
print(query)

result = conn.execute(query)
for row in result:
    print(row)

input("Press Enter ")

# distinct
query = select([country.c["Continent"]]).distinct()

print(query)

result = conn.execute(query)
for row in result:
    print(row)
