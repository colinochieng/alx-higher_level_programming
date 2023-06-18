#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py [username] [password] [database]
"""
import sys
import MySQLdb


def list_states(username, password, database):
   """ Connect to the MySQL server """
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states"
    cursor.execute(query)
    results = cursor.fetchall()
    # Display the results
    for row in results:
        print(row)

    # Close the database connection
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
