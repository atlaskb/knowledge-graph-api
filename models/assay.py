from pydantic import BaseModel


class Assay(BaseModel):
    name: str
