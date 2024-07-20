from pydantic import BaseModel

class FlowDto(BaseModel):
    name : str
    flow : int
