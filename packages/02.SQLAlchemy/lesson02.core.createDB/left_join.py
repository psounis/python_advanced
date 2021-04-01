from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
city = Table('city', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# left join
query = select([country.c["Name"].label("country"),
                func.count(city.c["Name"]).label("cities")]).\
        select_from(country.outerjoin(city, country.c["Code"] == city.c["CountryCode"])).\
        group_by(country.c["Name"])

result_set = conn.execute(query)
for row in result_set:
    print(row)

