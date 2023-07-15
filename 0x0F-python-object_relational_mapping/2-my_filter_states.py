#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Usage: ./2-my_filter_states.py [username] [password] [database] [state name]
"""
import sys
import MySQLdb


def filter_states(username, password, database, state):
    conn = MySQLdb.Connect(user=username, passwd=password, db=database)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM states WHERE name = '{}'
            ORDER BY states.id ASC""".format(state))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    filter_states(username, password, database, state)
