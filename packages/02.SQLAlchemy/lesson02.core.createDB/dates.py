from sqlalchemy.sql import insert, select
from sqlalchemy import create_engine, MetaData, Table, desc

engine = create_engine('mysql+mysqlconnector://root:root@localhost/pyworld')
metadata = MetaData()
dates = Table('dates', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# extract datetime
query = select([dates])
result = conn.execute(query).fetchall()

print(result[0])