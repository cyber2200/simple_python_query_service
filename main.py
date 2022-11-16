from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from models.Qbody import Qbody
from models.Db import Db
from models.Examples import Examples
app = FastAPI()

# --------------------------------------------------------
@app.post(
    "/q",
    response_model=Qbody,
    responses=Examples.qbody_responses

)
async def q(qbody: Qbody = Body(example= Examples.qbody_request_example)):
    db = Db()
    res = db.q(qbody.q, qbody.db)
    ret_code = 200
    if res['err'] != '':
        ret_code = 500
    
    return JSONResponse(content=res, status_code=ret_code)
# --------------------------------------------------------