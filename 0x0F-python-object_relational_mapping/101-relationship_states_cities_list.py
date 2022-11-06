#!/usr/bin/python3
"""
Relationship in sqlalchemy demo
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2],
            sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State).order_by(State.id)
    for state in result:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
