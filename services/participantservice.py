from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Participant as SchemaParticipant
from models import Participant as ModelParticipant


@app.post('/participant/', response_model=SchemaParticipant)
async def participant(participant:SchemaParticipant):
    db_participant = ModelParticipant(name=participant.name, age=participant.age)
    db.session.add(db_participant)
    db.session.commit()
    return db_participant

@app.get('/participant/')
async def participant():
    participant = db.session.query(ModelParticipant).all()
    return participant