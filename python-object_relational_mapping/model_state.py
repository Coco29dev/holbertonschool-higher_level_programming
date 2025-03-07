#!/usr/bin/python3

"""
Defines the State class for SQLAlchemy ORM.
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine("mysql+mysqldb://@localhost/")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
