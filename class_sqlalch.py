from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Device1(Base):
    __tablename__ = 'Devices'
    Id = Column(Integer,primary_key=True)
    ipAddress = Column(String(50), nullable=False)
    port = Column(String(50), nullable=False)
