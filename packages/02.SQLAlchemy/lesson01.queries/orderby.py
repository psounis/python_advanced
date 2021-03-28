from sqlalchemy.sql import select, desc
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# order by
query = select([country]).\
        where(country.c["Region"] == "Caribbean").\
        order_by(country.c["Name"])
result_set = conn.execute(query)
for row in result_set:
    print(row)


# order by desc
input("Press Enter to continue...")
query = select([country]).\
        where(country.c["Region"] == "Caribbean").\
        order_by(desc(country.c["Name"]))
result_set = conn.execute(query)
for row in result_set:
    print(row)


# order by 2 columns
input("Press Enter to continue...")
query = select([country.c["Name"], country.c["Region"]]).\
        order_by(country.c["Region"], desc(country.c["Name"]))
result_set = conn.execute(query)
for row in result_set:
    print(row)