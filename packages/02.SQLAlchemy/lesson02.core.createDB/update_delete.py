from sqlalchemy.sql import update, delete
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+mysqlconnector://root:root@localhost/sakila')
metadata = MetaData()
actor = Table('actor', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# update
query = update(actor).\
        where(actor.c["last_name"] == "Harelson").\
        values(last_name="Ali")
conn.execute(query)


# delete
input("Press Enter to continue: ")
query = delete(actor).\
        where(actor.c["actor_id"] >= 201)
conn.execute(query)

