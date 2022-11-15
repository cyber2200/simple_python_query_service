from pydantic import BaseModel

class Qbody(BaseModel):
    db: str
    q: str