from sqlalchemy.sql import select, or_, not_
from sqlalchemy import create_engine, MetaData, Table
from datetime import date

engine = create_engine('mysql+mysqlconnector://root:root@localhost/classicmodels')
metadata = MetaData()
products = Table('products', metadata, autoload=True, autoload_with=engine)
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

# where.where
query = select([products]).\
        where(products.c["productLine"] == "Classic Cars").\
        where(products.c["productVendor"] == "Min Lin Diecast")
result_set = conn.execute(query)
for row in result_set:
    print(row)


# bitwise & (and), | (or), ~ (not)
input("Press Enter to continue...")
query = select([products]).\
        where((products.c["productLine"] == "Classic Cars") \
              | ~ (products.c["productVendor"] == "Min Lin Diecast"))
result_set = conn.execute(query)
for row in result_set:
    print(row)

# methods: and_(), or_(), not_()
input("Press Enter to continue...")
query = select([products]).\
        where(or_(products.c["productLine"] == "Classic Cars"),
                 (not_(products.c["productVendor"] == "Min Lin Diecast")))
result_set = conn.execute(query)
for row in result_set:
    print(row)
