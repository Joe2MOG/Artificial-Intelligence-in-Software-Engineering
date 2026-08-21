#!/usr/bin/python3
"""Sets up a practice SQLite database with State and City models."""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    cities = relationship("City", back_populates="state")


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")


if __name__ == "__main__":
    engine = create_engine('sqlite:///orm_practice.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    new_york = State(name="New York")
    session.add_all([california, new_york])
    session.commit()

    session.add_all([
        City(name="Los Angeles", state=california),
        City(name="San Francisco", state=california),
        City(name="New York City", state=new_york),
        City(name="Buffalo", state=new_york)
    ])
    session.commit()
