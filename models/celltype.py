from pydantic import BaseModel


class CellType(BaseModel):
    name: str
