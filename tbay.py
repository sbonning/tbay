#This is the auction site code - for tbay 2.2.1
#6.12.17 Sam Bonning

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://samb@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

# a very strange thiing happened when I used "user" instead of "users", i could not commit/add additional users, it kept referending "current_user" with 1 row
# another Q: how do i recall a User?  like i saved "sammyb" as a user object but I can only currently look up by username or pword or primary key

class Bid(Base):
    __tablename__ = "bid"

    bid_id = Column(Integer, primary_key=True)
    price = Column(Float(2), nullable=False)

Base.metadata.create_all(engine)
