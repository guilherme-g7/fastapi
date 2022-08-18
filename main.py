from datetime import datetime
from typing import Dict, Union
from fastapi import FastAPI
from routes import router
from db.database import Base, engine, get_db
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from starlette import status
from fastapi.exceptions import HTTPException


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def alive() -> Dict[str, datetime]:
    return {"timestamps": datetime.now()}


app.include_router(router)