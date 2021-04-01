from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/classicmodels')
metadata = MetaData()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
offices = Table('offices', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()


sub = select([employees.c["employeeNumber"]]).\
      select_from(offices.join(employees, offices.c["officeCode"] == employees.c["officeCode"])).\
      where(offices.c["city"] == "San Francisco").subquery()

query = select([func.concat(employees.c["firstName"], " ", employees.c["lastName"]).label("supervisedSF")]).\
        where(employees.c["reportsTo"].in_(sub))

result_set = conn.execute(query)
for row in result_set:
    print(row)




