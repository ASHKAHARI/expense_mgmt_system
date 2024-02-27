from fastapi import FastAPI
import models
from database import SessionLocal,engine
from models import Expense
from fastapi.security import OAuth2PasswordBearer

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@app.post("/expense/")
async def create_expense(name: str, amount: float, category:str):
    db = SessionLocal()
    db_item = Expense(name=name, amount=amount,category=category)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/expenses/")
async def read_expenses():
    db = SessionLocal()
    item = db.query(Expense).all()
    return item


@app.get("/expenses/month/{year}/{month}/")
async def filter_expenses(year: int, month: int):
    db = SessionLocal()
    item = db.query(Expense).filter(created_at = year).all()
    return item