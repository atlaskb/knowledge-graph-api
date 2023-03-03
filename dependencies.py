from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header()):
    if x_token != "test-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "sooyoung":
        raise HTTPException(status_code=400, detail="No Sooyoung token provided")
