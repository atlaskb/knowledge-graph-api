from pydantic import BaseModel


class CellbyGene(BaseModel):
    cell: Cell
