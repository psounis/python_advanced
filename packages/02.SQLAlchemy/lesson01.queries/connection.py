from sqlalchemy import create_engine, MetaData, Table

conn_str = 'mysql+mysqlconnector://pythonuser:pwd1234@localhost/pyworld'
engine = create_engine(conn_str)
print(engine)
metadata = MetaData()
print(metadata.sorted_tables)

city = Table('city', metadata, autoload=True, autoload_with=engine)


print(city, city.columns["Name"])
conn = engine.connect()
print(conn)