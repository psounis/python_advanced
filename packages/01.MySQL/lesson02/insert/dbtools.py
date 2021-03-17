import mysql.connector
MYSQL = mysql.connector


def open_connection():
    try:
        return MYSQL.connect(
            host="localhost",
            user="pythonuser",
            password="pwd1234",
            database="pyworld"
        )
    except MYSQL.Error as e:
        print(e)


def close_connection(connection):
    try:
        connection.close()
    except MYSQL.Error as e:
        print(e)


# returns result set
def query_full_results(connection, query):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# iterator
def query_iter_one(connection, query):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            yield row
            row = cursor.fetchone()
        cursor.close()
    except MYSQL.Error as e:
        print(e)


# iterator
def query_iter_many(connection, n, query):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchmany(n)
    while rows:
        yield rows
        rows = cursor.fetchmany(n)
    cursor.close()


def insert_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)

    lastrowid = None
    if cursor.lastrowid:
        lastrowid = cursor.lastrowid

    cursor.close()

    return lastrowid
