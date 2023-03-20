#!/usr/bin/python3
"""
Prints the state Object passed as arument from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    arg = sys.argv[4]

    state = session.query(State).where(State.name == arg).first()
    if state:
        print(state.id)
    else:
        print("Not found")
