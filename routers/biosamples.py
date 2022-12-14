from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from dependencies import get_token_header

router = APIRouter(
    prefix="/biosamples",
    tags=["biosamples"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


class Biosample(BaseModel):
    name: str


fake_biosamples_db = {"first": {"name": "Sample 1"}, "second": {"name": "Sample 2"}}


@router.get("/")
async def read_biosamples():
    return fake_biosamples_db


@router.post("/")
async def create_biosample(biosample: Biosample):
    if biosample.name in fake_biosamples_db:
        raise HTTPException(status_code=404, detail="Biosample already created")
    return {"name": fake_biosamples_db[biosample.name]["name"], "biosample_id": biosample.name}


@router.get("/{biosample_id}")
async def read_biosample(biosample_id: str):
    if biosample_id not in fake_biosamples_db:
        raise HTTPException(status_code=404, detail="Biosample not found")
    return {"name": fake_biosamples_db[biosample_id]["name"], "biosample_id": biosample_id}


@router.put(
    "/{biosample_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_biosample(biosample_id: str):
    if biosample_id != "first":
        raise HTTPException(
            status_code=403, detail="You can only update the biosample: first"
        )
    return {"biosample_id": biosample_id, "name": "Sample 1"}


@router.delete("/{biosample_id}")
async def delete_biosample(biosample_id: str):
    return None
