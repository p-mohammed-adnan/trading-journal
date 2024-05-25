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
    notes = Column(String, nullable=True)  # Allow notes to be nullable
    status = Column(Boolean)

class TradePlan(Base):
    __tablename__ = 'trade_plans'

    id = Column(Integer, primary_key=True, index=True)
    ticker_symbol = Column(String)
    market = Column(String)
    position_type = Column(String)
    status = Column(String)
    rating = Column(Integer)
    account_size = Column(Float)
    account_risk_percent = Column(Float)
    entry_price = Column(Float)
    quantity = Column(Integer)
    stop_loss = Column(Float)
    target_price = Column(Float)
    roi = Column(Float)
    risk_reward = Column(Float)
    position_value = Column(Float)
    estimated_risk = Column(Float)
    estimated_profit = Column(Float)
    tags = Column(String)
