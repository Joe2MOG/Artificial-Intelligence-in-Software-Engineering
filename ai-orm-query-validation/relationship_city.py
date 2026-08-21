#!/usr/bin/python3
"""Defines the City class, linked to relationship_state's State."""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Represents a city, linked to the MySQL table cities."""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
