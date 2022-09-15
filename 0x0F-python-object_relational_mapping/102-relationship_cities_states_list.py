#!/usr/bin/python3
"""
Relationship in sqlalchemy demo
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2],
            sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    i = 1
    for res in session.query(State).join(City).all():
        for city in res.cities:
            print(f"{i}: {city.name} -> {res.name}")
            i += 1
