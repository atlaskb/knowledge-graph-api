from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header
from models import Participant

router = APIRouter(
    prefix="/participants",
    tags=["participants"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Participant)
async def create_participant(participant: Participant):
    return {"participant_name": participant.altName, "participant_id": participant.identifier}


@router.get("/{participant_id}")
async def read_participant(participant_id: int, q: Union[str, None] = None):
    return {"participant_id": participant_id, "q": q}


@router.put("/{participant_id}")
async def update_participant(participant_id: int, participant: Participant):
    return {"participant_name": participant.altName, "participant_id": participant_id}


@router.delete("/{participant_id}")
async def delete_participant(participant_id: int):
    return None
