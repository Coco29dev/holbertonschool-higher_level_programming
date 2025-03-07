#!/usr/bin/python3

"""
This script connects to a MySQL database
and lists all states from the 'states' table,
ordered by 'id'. It takes three arguments:
MySQL username, password, and database name.
"""


import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database,
        )

    cursor = mydb.cursor()

    query = ("SELECT cities.id, cities.name, states.name FROM\
                   cities INNER JOIN states ON\
                   cities.state_id = states.id WHERE states.name\
             = %s ORDER BY cities.id ASC")

    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()
    print(", ".join(city[1] for city in cities))

    cursor.close()
    mydb.close()
