from fastapi import FastAPI
from app.routers import trades
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(trades.router)
