
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Consumer(Base):
    __tablename__ = "consumers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    address = Column(String)

class Meter(Base):
    __tablename__ = "meters"
    id = Column(Integer, primary_key=True, index=True)
    meter_number = Column(String, unique=True)
    type = Column(String)
    consumer_id = Column(Integer, ForeignKey("consumers.id"))

class Reading(Base):
    __tablename__ = "readings"
    id = Column(Integer, primary_key=True, index=True)
    meter_id = Column(Integer, ForeignKey("meters.id"))
    value = Column(Float)

class Bill(Base):
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True, index=True)
    consumer_id = Column(Integer)
    amount = Column(Float)
    period = Column(String)
    status = Column(String)
