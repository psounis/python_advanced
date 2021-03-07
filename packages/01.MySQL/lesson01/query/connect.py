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
