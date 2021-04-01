from sqlalchemy.sql import insert, select
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+mysqlconnector://root:root@localhost/pyworld')
metadata = MetaData()
images = Table('images', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

with open("mysql.png", "rb") as f:
    contents = f.read()

# insert blob
query = insert(images).values(
                image=contents,
                descr="MySQL logo"
        )
result = conn.execute(query)
pk = result.inserted_primary_key

# extract blob
query = select([images.c["image"]]).\
        where(images.c["image_id"] == pk[0])
result = conn.execute(query).fetchall()

with open("copy.png", "wb") as f:
    f.write(result[0]["image"])