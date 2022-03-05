from enum import unique
from http.client import ImproperConnectionState
from database import Base
from sqlalchemy import String, Boolean,Integer,Column,Text, false


class Item(Base):
    __tablename__='items'
    id=Column(Integer, primary_key=True)
    car_model=Column(String(255),nullable=False, unique=True)
    trim_level=Column(Text)
    color=Column(String(255),nullable=False)
    price=Column(Integer,nullable=False)
    reserved=Column(Boolean,default=False)

    def __repr__(self):
        return f"<Item car_model={self.car_model} price={self.price}>"