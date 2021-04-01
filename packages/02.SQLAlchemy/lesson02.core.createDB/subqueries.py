from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# subquery

sub = select([func.avg(country.c["Population"])]).subquery()

query = select([country.c["Name"].label("country"),
                country.c["Population"]]).\
        where(country.c["Population"] > sub)

result_set = conn.execute(query)
for row in result_set:
    print(row)

