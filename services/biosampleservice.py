from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import BioSample as SchemaBioSample
from models import BioSample as ModelBioSample


@app.post('/biosample/', response_model=SchemaBioSample)
async def biosample(biosample: SchemaBioSample):
    db_biosample = ModelBioSample(name=biosample.name, biosample_id = biosample.biosample_id)
    db.session.add(db_biosample)
    db.session.commit()
    return db_biosample

@app.get('/biosample/')
async def biosample():
    biosample = db.session.query(ModelBioSample).all()
    return biosample
