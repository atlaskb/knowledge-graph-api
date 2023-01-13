from fastapi import Depends, FastAPI

from dependencies import get_query_token, get_token_header
# from internal import admin
from routers import biosamples, participants

import uvicorn
from fastapi_sqlalchemy import DBSessionMiddleware, db
import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(participants.router)
app.include_router(biosamples.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"message": "Knowledge Graph API"}


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)