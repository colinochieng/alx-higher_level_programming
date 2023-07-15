#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Usage: ./2-my_filter_states.py [username] [password] [database] [state]
"""
import sys
import MySQLdb


def cities_by_state(username, password, database, state):
    conn = MySQLdb.Connect(user=username, passwd=password, db=database)
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.name
                   FROM states INNER JOIN cities
                   ON states.id = cities.state_id
                   WHERE states.name LIKE BINARY '{}'""".format(state))
    result = cursor.fetchall()
    count = 1
    for row in result:
        if count < result.__len__():
                print(row[0], end=", ")
        else:
                print(row[0])
        count += 1
    cursor.close()
    conn.close()


if __name__ == "__main__":
    cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(";")[0])
