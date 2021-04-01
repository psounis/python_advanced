from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()


query = select([country.c["Continent"], func.count("*").label("Countries")]).\
        group_by(country.c["Continent"]).\
        having(func.count("*") > 50)
result_set = conn.execute(query)
for row in result_set:
    print(row)