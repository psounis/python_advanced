from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+mysqlconnector://root:root@localhost/classicmodels')
metadata = MetaData()
orderDetails = Table('orderDetails', metadata, autoload=True, autoload_with=engine)
offices = Table('offices', metadata, autoload=True, autoload_with=engine)
orders = Table('orders', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# between
query = select([orderDetails]).\
        where(orderDetails.c["priceEach"].between(100, 120))
result_set = conn.execute(query)
for row in result_set:
    print(row)


# in, notin
input("Press Enter to continue...")
query = select([offices]).\
        where(offices.c["city"].notin_(["Boston", "NYC"]))
result_set = conn.execute(query)
for row in result_set:
    print(row)


# NULL check
input("Press Enter to continue...")
query = select([orders]).\
        where(orders.c["comments"] != None)
result_set = conn.execute(query)
for row in result_set:
    print(row)


# LIKE, REGEXP
input("Press Enter to continue...")
query = select([orders]).\
        where(orders.c["comments"].like("Cust%")
              & orders.c["comments"].op("regexp")("(the.*){4}"))
result_set = conn.execute(query)
for row in result_set:
    print(row)
