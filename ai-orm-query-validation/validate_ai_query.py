#!/usr/bin/python3
"""Corrected ORM query: joins City and State using the relationship
property instead of a manual filter() equality check."""
from relationship_state import Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def validate_ai_query(username, password, db_name):
    """Prints every city with its state, using the state relationship.

    Connects to a MySQL database and lists all City objects together
    with the name of the State each one belongs to. The join is
    expressed through the ORM's relationship property rather than a
    manual filter() equality check, letting SQLAlchemy generate the
    correct SQL join automatically.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): name of the database to connect to.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} from {}".format(city.id, city.name, city.state.name))
    session.close()


if __name__ == "__main__":
    import sys
    validate_ai_query(sys.argv[1], sys.argv[2], sys.argv[3])
