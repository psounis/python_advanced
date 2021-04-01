
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Date, String, Enum, PrimaryKeyConstraint, Index, \
    ForeignKeyConstraint, CheckConstraint

engine = create_engine('mysql+mysqlconnector://root:root@localhost/emp2')
metadata = MetaData()

employees = Table('employees', metadata,
    Column('emp_no', Integer(), autoincrement=True),
    Column('birth_date', Date()),
    Column('first_name', String(30), nullable=False),
    Column('last_name', String(50), nullable=False),
    Column('gender', Enum('M', 'F'), nullable=False, default='M'),
    Column('hire_date', Date(), nullable=False),
    PrimaryKeyConstraint('emp_no', name='emp_pk')
)

departments = Table('departments', metadata,
    Column('dept_no', String(4)),
    Column('dept_name', String(40), nullable=False, unique=True),
    PrimaryKeyConstraint('dept_no', name='dept_pk'),
    Index('dept_name_idx', 'dept_name')
)

dept_emp = Table('dept_emp', metadata,
    Column('emp_no', Integer),
    Column('dept_no', String(4)),
    Column('from_date', Date(), nullable=False),
    Column('to_date', Date(), nullable=False),
    PrimaryKeyConstraint('emp_no', 'dept_no', name='dept_emp_pk'),
    ForeignKeyConstraint(('emp_no',), ["employees.emp_no"], name="fk1"),
    ForeignKeyConstraint(('dept_no',), ["departments.dept_no"], name="fk2"),
    CheckConstraint('from_date < to_date', name="chk_date")
)

metadata.create_all(engine)

conn = engine.connect()