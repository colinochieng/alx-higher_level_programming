#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
It takes 3 arguments: mysql username, mysql password and database name
Usage: ./9-model_state_filter_a.py [uname] [passwd] [db name]
Results are sorted in ascending order by states.id
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

    for row in session.query(State).order_by(State.id).all():
        print(str(row.id) + ': ' + row.name)

    session.close()
