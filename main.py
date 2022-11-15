from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.Qbody import Qbody
from models.Db import Db

app = FastAPI()

@app.post("/q")
async def q(qbody: Qbody):
    db = Db()
    res = db.q(qbody.q, qbody.db)
    return JSONResponse(content=res)