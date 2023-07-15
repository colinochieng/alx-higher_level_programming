#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Usage: ./2-my_filter_states.py [username] [password] [database]
"""
import sys
import MySQLdb


def cities_by_state(username, password, database):
    conn = MySQLdb.Connect(user=username, passwd=password, db=database)
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM states INNER JOIN cities
                   ON states.id = cities.state_id
                   ORDER BY cities.id""")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
