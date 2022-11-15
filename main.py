from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from models.Qbody import Qbody
from models.Db import Db

app = FastAPI()

# --------------------------------------------------------
qbody_example = {
    "res": "OK",
    "q_res": [
        {
            "id": "1",
            "msg": "123",
            "ts": "2022-11-15 19:45:12"
        }
    ]
}

@app.post("/q")
async def q(qbody: Qbody = Body(example = qbody_example)):
    db = Db()
    res = db.q(qbody.q, qbody.db)
    return JSONResponse(content=res)
# --------------------------------------------------------