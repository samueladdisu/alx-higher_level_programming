#!/usr/bin/python3
"""
script to list all state with sqlalchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3036/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State).order_by(State.id).all()
    for r in result:
        print(f"{r.id}: {r.name}")
