from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
city = Table('city', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# limit
query = select([city]).\
        order_by(city.c["ID"]).\
        limit(100)
result_set = conn.execute(query)
for row in result_set:
    print(row)


# limit with offset
input("Press Enter to continue...")
query = select([city]).\
        order_by(city.c["ID"]).\
        limit(100).offset(100)
result_set = conn.execute(query)
for row in result_set:
    print(row)