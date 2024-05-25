from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TradeBase(BaseModel):
    date: datetime
    ticker_symbol: str
    entry_price: float
    exit_price: float
    quantity: int
    trade_type: str
    notes: Optional[str] = None  # Make notes optional
    status: bool

class TradeCreate(TradeBase):
    pass

class Trade(TradeBase):
    id: int

    class Config:
        from_attributes = True
