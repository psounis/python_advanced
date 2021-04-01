from sqlalchemy.sql import select, desc
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

query = select([country.c["Continent"],
                func.count("*").label("Countries"),
                func.avg(country.c["Population"]).label("avg_population")]).\
        where(country.c["IndepYear"] != None).\
        group_by(country.c["Continent"]).\
        having((func.count("*") > 10)
               & (func.min(country.c["SurfaceArea"]) > 10)).\
        order_by(desc(func.count("*"))).\
        limit(2)

result_set = conn.execute(query)
for row in result_set:
    print(row)
