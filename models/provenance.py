from pydantic import BaseModel


class Provenance(BaseModel):
    name: str
