from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
city = Table('city', metadata, autoload=True, autoload_with=engine)
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# select *
query = select([city])
result_set = conn.execute(query)
for row in result_set:
    print(row)

# select columns
input("Press Enter to continue...")
query = select([city.c.ID, city.c.Name])
result_set = conn.execute(query)
for row in result_set:
    print(row)


# select distinct
input("Press Enter to continue...")
query = select([country.c["Continent"]]).distinct()
result_set = conn.execute(query)
for row in result_set:
    print(row)