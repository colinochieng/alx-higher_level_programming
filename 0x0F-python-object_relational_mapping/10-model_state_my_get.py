#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
It takes 4 arguments: mysql username, mysql password and database name
and state name to search (SQL injection free)
Usage: ./10-model_state_my_get.py [uname] [passwd] [db name] [state name]
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

    row = session.query(State).filter_by(name=argv[4]).first()
    if row:
        print(row.id)
    else:
        print("Not found")

    session.close()
