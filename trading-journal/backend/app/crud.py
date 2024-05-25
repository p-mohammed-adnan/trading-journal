from sqlalchemy.orm import Session
from app import models, schemas

def get_trade(db: Session, trade_id: int):
    return db.query(models.Trade).filter(models.Trade.id == trade_id).first()

def create_trade(db: Session, trade: schemas.TradeCreate):
    db_trade = models.Trade(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def get_trades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trade).offset(skip).limit(limit).all()

def get_trade_plan(db: Session, trade_plan_id: int):
    return db.query(models.TradePlan).filter(models.TradePlan.id == trade_plan_id).first()

def create_trade_plan(db: Session, trade_plan: schemas.TradePlanCreate):
    trade_plan_dict = trade_plan.dict()
    trade_plan_dict['roi'] = ((trade_plan.target_price - trade_plan.entry_price) / trade_plan.entry_price) * 100
    trade_plan_dict['risk_reward'] = (trade_plan.target_price - trade_plan.entry_price) / (trade_plan.entry_price - trade_plan.stop_loss)
    trade_plan_dict['position_value'] = trade_plan.entry_price * trade_plan.quantity
    trade_plan_dict['estimated_risk'] = (trade_plan.entry_price - trade_plan.stop_loss) * trade_plan.quantity
    trade_plan_dict['estimated_profit'] = (trade_plan.target_price - trade_plan.entry_price) * trade_plan.quantity
    db_trade_plan = models.TradePlan(**trade_plan_dict)
    db.add(db_trade_plan)
    db.commit()
    db.refresh(db_trade_plan)
    return db_trade_plan

def update_trade_plan(db: Session, trade_plan_id: int, trade_plan: schemas.TradePlanCreate):
    db_trade_plan = db.query(models.TradePlan).filter(models.TradePlan.id == trade_plan_id).first()
    if db_trade_plan:
        for key, value in trade_plan.dict().items():
            setattr(db_trade_plan, key, value)
        db.commit()
        db.refresh(db_trade_plan)
    return db_trade_plan

def delete_trade_plan(db: Session, trade_plan_id: int):
    db_trade_plan = db.query(models.TradePlan).filter(models.TradePlan.id == trade_plan_id).first()
    if db_trade_plan:
        db.delete(db_trade_plan)
        db.commit()
    return db_trade_plan

def get_trade_plans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TradePlan).offset(skip).limit(limit).all()
