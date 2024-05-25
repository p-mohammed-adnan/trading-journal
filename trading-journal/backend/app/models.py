from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from app.database import Base

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    ticker_symbol = Column(String)
    entry_price = Column(Float)
    exit_price = Column(Float)
    quantity = Column(Integer)
    trade_type = Column(String)
    notes = Column(String)
    status = Column(Boolean)
