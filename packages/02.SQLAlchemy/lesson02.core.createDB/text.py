from sqlalchemy.sql import select, text
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/world')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# text query
query = text("SELECT * FROM country")

result_set = conn.execute(query)
for row in result_set:
    print(row)


# text inside query
input("Press Enter to continue")
query = select([country.c["Name"].label("country"),
                country.c["Population"]]).\
        where(text("country.Name > 'X' AND country.Population > 10000"))

result_set = conn.execute(query)
for row in result_set:
    print(row)

