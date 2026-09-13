from pydantic import BaseModel

class AskRequest(BaseModel):
    query: str

class AskResponse(BaseModel):
    query: str
    route: str
    response: str