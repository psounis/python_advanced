from sqlalchemy.sql import update
from sqlalchemy import create_engine, MetaData, Table, desc

engine = create_engine('mysql+mysqlconnector://root:root@localhost/pyworld')
metadata = MetaData()
country = Table('country', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# update
query = update(country).\
        where((country.c["HeadOfState"] == "Elisabeth II")
              | (country.c["HeadOfState"] == "Jacques Chirac")).\
        values(HeadOfState="Boris Johnson")
conn.execute(query)