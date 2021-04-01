from datetime import date, datetime, timedelta

from sqlalchemy.sql import insert, select
from sqlalchemy import create_engine, MetaData, Table, desc, func

engine = create_engine('mysql+mysqlconnector://root:root@localhost/emp2')
metadata = MetaData()
departments = Table('departments', metadata, autoload=True, autoload_with=engine)
employees = Table('employees', metadata, autoload=True, autoload_with=engine)
dept_emp = Table('dept_emp', metadata, autoload=True, autoload_with=engine)
conn = engine.connect()

transaction = conn.begin()

try:
    # an insert to departments
    query = insert(departments).values(
                    dept_no = "LOG",
                    dept_name = "Logistics"
            )
    conn.execute(query)

    # insert to employees
    query = insert(employees).values(
                    birth_date = date(1980, 5, 2),
                    first_name = "Eva",
                    last_name = "Green",
                    gender = 'F',
                    hire_date = datetime.now().date() - timedelta(days=20)
            )
    result = conn.execute(query)
    pk = result.inserted_primary_key[0]

    # insert to dept_emp
    query = insert(dept_emp).values(
                    dept_no = "LOG",
                    emp_no = pk,
                    from_date = datetime.now().date() - timedelta(days=20),
                    to_date = datetime.now().date(),
            )
    result = conn.execute(query)

    transaction.commit()
except Exception:
    transaction.rollback()
    print("An error occurred: The transaction was not completed.")
