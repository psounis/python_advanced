from sqlalchemy.sql import insert, select
from sqlalchemy import create_engine, MetaData, Table, desc

engine = create_engine('mysql+mysqlconnector://root:root@localhost/sakila')
metadata = MetaData()
actor = Table('actor', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# an insert
query = insert(actor).values(
                first_name = "Woody",
                last_name = "McConaughey"
        )
result = conn.execute(query)
print(result.inserted_primary_key)


# multiple inserts
result = conn.execute(insert(actor), [
        {"first_name": "Matthew", "last_name":"Harelson"},
        {"first_name": "Colin", "last_name": "McAdams"}
])

# insert into... select
select_query = select([actor.c["first_name"], actor.c["last_name"]]).\
               where(actor.c["last_name"].like('o%'))
insert_query = insert(actor).\
               from_select(["first_name", "last_name"], select_query)
conn.execute(insert_query)
