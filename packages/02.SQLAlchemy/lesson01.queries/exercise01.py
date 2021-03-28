from sqlalchemy.sql import select, desc
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()


query = select([country.c["Continent"], country.c["Region"], func.count("*").label("Countries")]).\
        where(country.c["Continent"].in_(["Asia", "Europe", "Africa"])).\
        group_by(country.c["Continent"], country.c["Region"]).\
        order_by(country.c["Continent"], desc(country.c["Region"])).\
        limit(10)
result_set = conn.execute(query)
for row in result_set:
    print(row)