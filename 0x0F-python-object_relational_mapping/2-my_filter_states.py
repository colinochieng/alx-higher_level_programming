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
    cursor.execute("""SELECT * FROM states 
                   WHERE name LIKE BINARY '{}' 
                   ORDER BY states.id ASC""".format(state).strip("'"))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    conn.close()


# if __name__ == "__main__":
#     username = sys.argv[1]
#     password = sys.argv[2]
#     database = sys.argv[3]
#     state = sys.argv[4]
#     filter_states(username, password, database, state)

if __name__ == '__main__':
    if len(sys.argv) >= 5:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db_connection.cursor()
        state_name = sys.argv[4]
        cursor.execute(
            'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
            'CAST("{}" AS BINARY) ORDER BY id ASC;'.format(state_name)
        )
        results = cursor.fetchall()
        for result in results:
            print(result)
        db_connection.close()
