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

class TradePlanBase(BaseModel):
    ticker_symbol: str
    market: str
    position_type: str
    status: str
    rating: int
    account_size: Optional[float] = 10000.0
    account_risk_percent: float
    entry_price: float
    quantity: int
    stop_loss: float
    target_price: float
    tags: Optional[str] = None  # Make tags optional

    class Config:
        from_attributes = True

class TradePlanCreate(TradePlanBase):
    pass

class TradePlan(TradePlanBase):
    id: int
    roi: float
    risk_reward: float
    position_value: float
    estimated_risk: float
    estimated_profit: float

    class Config:
        orm_mode = True
