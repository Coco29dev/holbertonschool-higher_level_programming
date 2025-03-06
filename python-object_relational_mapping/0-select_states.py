#!/usr/bin/python3

import MySQLdb
import sys


"""
This script connects to a MySQL database
and lists all states from the 'states' table,
ordered by 'id'. It takes three arguments:
MySQL username, password, and database name.
"""


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    mydb = MySQLdb.connect(
        host="localhost",
        user="root",
        password="root",
        database="hbtn_0e_0_usa"
        )

    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    mydb.close()
