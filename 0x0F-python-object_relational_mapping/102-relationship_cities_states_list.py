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
    Using Backref navigation:
        results = session.query(City).all()
    <city id>: <city name> -> <state name>
    """
    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
