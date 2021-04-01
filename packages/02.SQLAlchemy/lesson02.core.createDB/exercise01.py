from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table, desc
from sqlalchemy import func
engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
city = Table('city', metadata, autoload=True, autoload_with=engine)
countrylanguage = Table('countrylanguage', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# inner join
query = select([city.c["Name"].label("city"),
                city.c["Population"].label("population"),
                func.count("*").label("languages_spoken")]).\
        select_from(city.\
                join(country, city.c["CountryCode"] == country.c["Code"]). \
                join(countrylanguage, country.c["Code"] == countrylanguage.c["CountryCode"])).\
        where(country.c["Name"] == "Greece").\
        group_by(city.c["Name"]).\
        order_by(desc(city.c["Population"])).\
        limit(2)
result_set = conn.execute(query)
for row in result_set:
    print(row)

