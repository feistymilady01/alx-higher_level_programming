#!/usr/bin/python3
"""
Class definition of a State and an instance Base
"""

from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):

    """
    Class State that inherits from Base and links to the
    MySQL table state in database hbtn_0e_6_usa.states
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
