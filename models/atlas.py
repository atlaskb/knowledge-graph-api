from pydantic import BaseModel


class Atlas(BaseModel):
    type: Spatial, Dimensional
