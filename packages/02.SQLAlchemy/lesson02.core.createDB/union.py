from sqlalchemy.sql import select, union
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/classicmodels')
metadata = MetaData()
customers = Table('customers', metadata, autoload=True, autoload_with=engine)
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# union

query = union(
            select([customers.c["contactLastName"].label("lastName")]),
            select([employees.c["lastName"]])
            )

result_set = conn.execute(query)
for row in result_set:
    print(row)

