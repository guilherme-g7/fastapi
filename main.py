from datetime import datetime
from typing import Dict, Union
from fastapi import FastAPI
from routes import router
from db.database import Base, engine, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def alive() -> Dict[str, datetime]:
    return {"timestamps": datetime.now()}


app.include_router(router)
