from datetime import datetime
from typing import Dict

from fastapi import FastAPI
from routes import router
from db.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def alive() -> Dict[str, datetime]:
    return {"timestamps": datetime.now()}


app.include_router(router)
