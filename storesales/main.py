# main.py
from datetime import datetime
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .api import auth, goods, sale, restock
from storesales.db.session import engine  # Make sure this import matches your project structure
from storesales.models.base_class import Base  # Adjust this import based on your project's structure

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()
app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(goods.router, prefix="/goods", tags=["goods"])
app.include_router(sale.router, prefix="/sale", tags=["sale"])
app.include_router(restock.router, prefix="/restock", tags=["restock"])

@app.on_event("startup")
async def startup_event():
    # Place for startup events like initializing connections or logging
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Cleanup actions on shutdown, like closing database connections
    pass

# Example root endpoint
@app.get("/")
async def root():
    return {"message": "Hello, World!"}
