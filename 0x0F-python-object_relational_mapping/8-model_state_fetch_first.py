#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
It takes 3 arguments: mysql username, mysql password and database name
Usage: ./8-model_state_fetch_first.py [uname] [passwd] [db name]
"""
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).first()
    if row:
        print(str(row.id) + ': ' + row.name)
    else:
        print("Nothing")

    session.close()
