from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# aggregate
query = select([func.count(country.c["IndepYear"]).label("count")])
result_set = conn.execute(query)
for row in result_set:
    print(row)

# count *
input("Press Enter to continue...")
query = select([func.count("*").label("count")]).\
        select_from(country)
result_set = conn.execute(query)
for row in result_set:
    print(row)


# group by
input("Press Enter to continue...")
query = select([country.c["Continent"], country.c["Region"], func.count("*").label("Countries")]).\
        group_by(country.c["Continent"], country.c["Region"])
result_set = conn.execute(query)
for row in result_set:
    print(row)