
from datetime import datetime
from sqlalchemy import  Column, Integer, String,Float,DateTime


from database import Base




class Expense(Base):
    __tablename__ = "Expense"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    amount = Column(Float, index=True)
    category = Column(String)
    created_at =  Column(DateTime, default=datetime.utcnow)

    