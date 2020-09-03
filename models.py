from database import Base 
from sqlalchemy import Column, Integer, JSON
import sqlalchemy.types as types 

class PrimeNumber(Base):
    __tablename__ = "prime_numbers"

    id = Column(Integer, primary_key=True, index=True)
    base_number = Column(Integer, nullable=False, unique=True)
    result = Column(JSON, nullable=False)


class PrimeTwin(Base):
    __tablename__ = "prime_twins"

    id = Column(Integer, primary_key=True, index=True)
    base_number = Column(Integer, nullable=False, unique=True)
    result = Column(JSON, nullable=False)