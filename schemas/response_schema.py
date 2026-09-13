from pydantic import BaseModel
class AgentResponse(BaseModel):
    query: str
    route:str
    response: str