#!/usr/bin/python3
"""
python file that contains the class definition of
a State and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """Class to create states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref='state')
