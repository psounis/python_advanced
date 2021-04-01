from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from datetime import date

engine = create_engine('mysql+mysqlconnector://root:root@localhost/classicmodels')
metadata = MetaData()
products = Table('products', metadata, autoload=True, autoload_with=engine)
orders = Table('orders', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# inequality
query = select([products.c["productName"], products.c["quantityInStock"]]).\
        where(products.c["quantityInStock"] >= 9000)
result_set = conn.execute(query)
for row in result_set:
    print(row)


# equality
input("Press Enter to continue...")
query = select(products).\
        where(products.c["productVendor"] == "WELLY DIECAST PRODUCTIONS")
result_set = conn.execute(query)
for row in result_set:
    print(row)


# not equal
input("Press Enter to continue...")
query = select([orders.c["orderNumber"], orders.c["orderDate"], orders.c["status"]]).\
        where(orders.c["orderDate"] != date(2005, 5, 31))
result_set = conn.execute(query)
for row in result_set:
    print(row)

