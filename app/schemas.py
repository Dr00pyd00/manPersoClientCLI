from pydantic import BaseModel 
from datetime import datetime

class ManPageCreateSchema(BaseModel):
    title: str 
    summary: str | None = None 
    text: str 
    tags: list[str] = []


class ManPageDisplayFullSchema(BaseModel):
    id: int 
    title: str 
    summary: str | None = None 
    text: str
    tags: list = [] 



