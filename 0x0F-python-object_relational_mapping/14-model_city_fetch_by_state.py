#!/usr/bin/python3
"""
script to list all cties with sqlalchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3036/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(
        State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id).all()
    for r in result:
        print(f"{r[0]}: ({r[1]}) {r[2]}")
