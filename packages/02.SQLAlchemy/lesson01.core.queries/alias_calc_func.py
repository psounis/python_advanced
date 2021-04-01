from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://pythonuser:pwd1234@localhost/pyworld')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
city = Table('city', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# alias
query = select([city.c["ID"].label("city_id"), city.c["Name"]])
result_set = conn.execute(query)
for row in result_set:
    print(row)

# calculated columns
input("Press Enter to continue...")
query = select(country.c["Name"].label("country"),
               (2021-country.c["IndepYear"]).label("years_free"))
result_set = conn.execute(query)
for row in result_set:
    print(row)

# DBMS functions
input("Press Enter to continue...")
query = select(func.concat(country.c["HeadOfState"], " of ",
                           country.c["Name"]).label("country"))
result_set = conn.execute(query)
for row in result_set:
    print(row)

