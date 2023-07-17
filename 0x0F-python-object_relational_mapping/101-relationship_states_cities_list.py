#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects
contained in the database hbtn_0e_101_usa
Takes 3 arguments: mysql username, mysql password and database name
Usage: ./101-relationship_states_cities_list.py [uname] [passwd] [db]
"""
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine
from sys import argv
from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    """
    Using Simple join() method
    query = session.query(State, City).join(City, State.id == City.state_id)
    results = query.all()

    Eager loading using options():
        query = session.query(State).options(joinedload(State.cities))
        results = query.all()
    Relationship navigation:
        results = session.query(State).all()
    Backref navigation:
        results = session.query(City).all()
    <state id>: <state name>
    <tabulation><city id>: <city name>
    """
    results = session.query(State).all()
    for state in results:
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
