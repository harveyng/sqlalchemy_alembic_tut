from datetime import datetime

from sqlalchemy.orm import declarative_base 
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime, default=datetime.utcnow)
    