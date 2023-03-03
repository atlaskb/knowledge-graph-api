from pydantic import BaseModel


class Location(BaseModel):
    photo: Photo
    coordinates: [str, str]
    atlasMap: dict(Atlas)
    atlas: Atlas
    overlappingLabels: [str, str]
