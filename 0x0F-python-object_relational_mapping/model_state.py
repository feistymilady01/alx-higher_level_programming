#!/usr/bin/python3
"""
Class definition of a City and an instance Base
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

# mymetadata = MetaData()
# Base = declarative_base(metadata=mymetadata)


class City(Base):

    """
    Class City that inherits from Base and links to the
    MySQL table cities in database hbtn_0e_6_usa.states
    """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
