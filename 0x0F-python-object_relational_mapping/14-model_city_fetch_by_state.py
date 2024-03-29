#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa
It takes 3 arguments: mysql username, mysql password and database name
Usage: ./14-model_city_fetch_by_state.py [uname] [passwd] [db name]
Results display as  (<state name>: (<city id>) <city name>)
"""
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City)\
            .filter(City.state_id == State.id).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
