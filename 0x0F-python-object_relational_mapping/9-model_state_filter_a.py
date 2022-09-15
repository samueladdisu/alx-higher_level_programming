#!/usr/bin/python3
"""
script first state object
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, dbname))
    session = sessionmaker(bind=engine)()
    result = session.query(State).filter(State.name.contains("a")).all()
    for r in result:
        print(f"{r.id}: {r.name}")
