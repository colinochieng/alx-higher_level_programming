#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Usage: ./2-my_filter_states.py [username] [password] [database] [state]
"""
import sys
import MySQLdb


def cities(username, password, database, state):
    conn = MySQLdb.Connect(user=username, passwd=password, db=database)
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.name, states.name
                   FROM states INNER JOIN cities
                   ON states.id = cities.state_id""")
    result = cursor.fetchall()
    
    output = ', '.join(row[0] for row in result if row[1] == state)
    print(output)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
