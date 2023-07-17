#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
It takes 3 arguments: mysql username, mysql password and database name
Usage: ./7-model_state_fetch_all.py [uname] [passwd] [db name]
"""
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}""".
                       format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

for row in session.query(State).all():
    print(str(row.id) + ': ' + row.name)

session.close()
