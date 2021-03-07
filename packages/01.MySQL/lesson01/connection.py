import mysql.connector
MYSQL = mysql.connector

try:
    with MYSQL.connect(
        host="localhost",
        user="pythonuser",
        password="pwd1234",
        database="pyworld"
    ) as connection:
        # program code goes here
        print(connection)
except MYSQL.Error as e:
    print(e)




