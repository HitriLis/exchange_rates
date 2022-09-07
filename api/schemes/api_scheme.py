from pydantic import BaseModel

class BodyMessage(BaseModel):
    status: int
    message: str
