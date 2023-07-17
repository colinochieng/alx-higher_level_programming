#!/usr/bin/python3
"""
python file that contains the class definition of
a State and an instance Base = declarative_base()
"""
from relationship_state import Base
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy import ForeignKey


class City(Base):
    """
    Creates a class City that references the states via its id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
