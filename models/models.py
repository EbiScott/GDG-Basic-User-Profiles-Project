from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, auto_increment=True)
    name = Column(String, nullable=False)
    ## I need to find out how to record emails ---> that's part of the focus points
    email = Column(String, nullable=False, unique=True)
    bio = Column(String)