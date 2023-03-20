#!/usr/bin/python3
"""
Updates a State object to the datebase
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

    del_states = session.query(State).where(State.name.like('%a%'))
    for state in del_states:
        session.delete(state)

    # session.add(updt_state)
    session.commit()

    session.close()
