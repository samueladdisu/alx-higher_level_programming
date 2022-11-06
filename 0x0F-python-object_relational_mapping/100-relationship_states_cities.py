#!/usr/bin/python3
"""
Relationship in sqlalchemy demo
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from relationship_city import City, Base
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2],
            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
