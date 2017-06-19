#This is the auction site code - for tbay 2.2.1
#6.12.17 Sam Bonning

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://samb@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    item = relationship("Item", backref="users")
    bid = relationship("Bid",backref="users")

class Item(Base):
    __tablename__ = "item"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bid = relationship("Bid",backref="item")

# another Q: how do i recall a User?  like i saved "sammyb" as a user object but I can only currently look up by username or pword or primary key

class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    price = Column(Float(2), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)

Base.metadata.create_all(engine)

cassie = User(username="Cassie", password="cats")
alex = User(username="Alex", password="cats")
sandra = User(username="Sandra", password="bbq")

baseball = Item(name="baseball", users=alex)

bid1 = Bid(price=2, users=cassie, item=baseball)
bid2 = Bid(price=3, users=sandra, item=baseball)

# session.add_all([cassie, alex, sandra, baseball, bid1, bid2])
# session.commit()

for bid in baseball.bid:
    print (baseball.name + " " + str(bid.price) + " " + bid.users.username)

print (session.query(Bid.price, Bid.users).join(User).filter(Item.name == "baseball").order_by(Bid.price.desc()).all())

# hi emily, still having trouble.  Trying to pull out the user from the bid in my session.query - i've tried everything Bid.users.username, Bid.users etc.  I either get a weird set of True/False or I get an error.









