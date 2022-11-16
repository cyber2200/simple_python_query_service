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
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": Examples.qbody_response_example
                }
            },
        },
    },

)
async def q(qbody: Qbody = Body(example= Examples.qbody_request_example)):
    db = Db()
    res = db.q(qbody.q, qbody.db)
    return JSONResponse(content=res)
# --------------------------------------------------------