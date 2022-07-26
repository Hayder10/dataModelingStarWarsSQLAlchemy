import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ignore = Column(Integer,primary_key=True)
    user_from_id = Column(Integer,ForeignKey('user.id'))
    user_to_id = Column(Integer,ForeignKey('user.id'))


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), ForeignKey('person.id'))
    followers = relationship('Follower')
    comment = relationship('Comment')
    post = relationship('Post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id')) #Foreign Key of user.id
    post_id = Column(Integer, ForeignKey('post.id')) #Foreign Key of post.id

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id')) #Foreign key of user.id
    comment = relationship('Comment')
    post = relationship('Media')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer,ForeignKey('post.id')) #Foreign key of post.id


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')