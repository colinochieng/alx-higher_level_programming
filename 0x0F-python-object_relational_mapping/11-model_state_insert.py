#!/usr/bin/python3
"""
script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa
It takes 3 arguments: mysql username, mysql password and database name
Usage: ./11-model_state_insert.py [uname] [passwd] [db name]
"""
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    new_state = State()
    new_state.name = "Louisiana"
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
