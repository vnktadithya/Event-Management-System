from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user' # Explicitly setting tablename is good practice

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(128), nullable=False) # Added password field (for hashed password)
    dept = Column(String(50))

class Event(Base):
    __tablename__ = 'event'

    event_id = Column(Integer, primary_key=True)
    event_name = Column(String(100), nullable=False)
    event_type = Column(String(50))
    date = Column(Date)
    venue = Column(String(100))
    organised_by = Column(Integer, ForeignKey('user.user_id'))
    description = Column(Text)

class Register(Base):
    __tablename__ = 'register'

    reg_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    status = Column(String(20))
    reg_date = Column(Date)
    event_id = Column(Integer, ForeignKey('event.event_id'))

class Event_Coordinator(Base):
    __tablename__ = 'event_coordinator'

    coordinator_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    event_id = Column(Integer, ForeignKey('event.event_id'))
    role = Column(String(50))

class Feedback(Base):
    __tablename__ = 'feedback'

    f_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    event_id = Column(Integer, ForeignKey('event.event_id'))
    rating = Column(Integer)
    feedback = Column(Text)
    comments = Column(Text)