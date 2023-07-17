#!/usr/bin/python3
"""
script changes the name of a State object from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico
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
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).get(2)
    data.name = "New Mexico"
    session.commit()

    session.close()
