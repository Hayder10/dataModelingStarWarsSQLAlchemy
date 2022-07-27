import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer,primary_key=True)
    planet_id = Column(Integer,ForeignKey('planets.id')) #Foreign key of planets.id
    character_id = Column(Integer,ForeignKey('characters.id')) #Foreign key of characters.id
    user_id = Column(Integer,ForeignKey('user.id')) #Foreign key of user.id
    vehicle_id = Column(Integer,ForeignKey('vehicles.id')) #Foreign key of vehicles.id


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    password = Column(String(250))
    email = Column(String(250), unique=True)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gravity = Column(Integer)
    terrain = Column(String(250))
    population = Column(Integer)
    

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    gender = Column(String(250))
    vehicle_id = Column(Integer,ForeignKey('vehicles.id')) #Foreign key of vehicles.id


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    cost = Column(Integer)
    max_speed = Column(Integer)
    pilots = Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')