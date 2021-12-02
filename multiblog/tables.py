from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    blog_name = Column(String(144), unique=False)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String(144), unique=False)
    author_surname = Column(String(144), unique=False)
    blog_id = Column(Integer, ForeignKey('blogs.id'), nullable=True)

    blog = relationship("Blog", backref=backref("authors", uselist=False))


class Publication(Base):
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_title = Column(String(144), unique=False)
    post_date = Column(DateTime, unique=False)


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_title = Column(String(32), unique=True)