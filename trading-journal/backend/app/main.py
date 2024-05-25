import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import trades
from app.database import engine, Base

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# Allow CORS
origins = [
    "http://localhost:3000",  # Frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

Base.metadata.create_all(bind=engine)

app.include_router(trades.router)
