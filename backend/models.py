from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False) 
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False) 
    is_admin = Column(Integer, default=0) 

    queries = relationship("WeatherQuery", back_populates="owner")


# class Query(Base):
#     __tablename__ = "queries"
#     id = Column(Integer, primary_key=True, index=True)
#     location = Column(String)
#     temperature = Column(String)
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User", back_populates="queries")


class WeatherQuery(Base):
    __tablename__ = "weather_queries"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    temperature = Column(Float)
    condition = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="queries")

