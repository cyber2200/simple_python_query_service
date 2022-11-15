from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models.Db import Db
import mysql.connector

class Qbody(BaseModel):
    db: str
    q: str

app = FastAPI()

@app.post("/q")
async def q(qbody: Qbody):
    db = Db()
    res = db.q(qbody.q, qbody.db)
    return JSONResponse(content=res)