from pydantic import BaseModel


class Cell(BaseModel):
    location: str
    cellType: CellType
