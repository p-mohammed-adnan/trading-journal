from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/trades/", response_model=schemas.Trade)
def create_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    return crud.create_trade(db=db, trade=trade)

@router.get("/trades/", response_model=List[schemas.Trade])
def read_trades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trades = crud.get_trades(db, skip=skip, limit=limit)
    return trades

@router.get("/trades/{trade_id}", response_model=schemas.Trade)
def read_trade(trade_id: int, db: Session = Depends(get_db)):
    db_trade = crud.get_trade(db, trade_id=trade_id)
    if db_trade is None:
        raise HTTPException(status_code=404, detail="Trade not found")
    return db_trade
