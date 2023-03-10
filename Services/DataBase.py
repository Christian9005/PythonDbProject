import mysql.connector

def Connection_DB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ckrisfoxx;13A#",
        database="dbproject"
    )
    return mydb

