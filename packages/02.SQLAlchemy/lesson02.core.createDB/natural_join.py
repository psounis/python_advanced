from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+mysqlconnector://root:root@localhost/classicmodels')
metadata = MetaData()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
offices = Table('offices', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# natural join
query = select([offices.c["city"], employees.c["lastName"]]).\
        select_from(offices.join(employees))

result_set = conn.execute(query)
for row in result_set:
    print(row)

# cross join
input("Press Enter to continue...")
query = select([offices, employees])
result_set = conn.execute(query)
for row in result_set:
    print(row)




