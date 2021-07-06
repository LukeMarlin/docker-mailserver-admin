import os
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import APIKeyHeader

_api_key_header = APIKeyHeader(name="X-API-KEY")


async def check_api_key(key: str = Depends(_api_key_header)):
    if key != os.getenv("DOCKER_MAILSERVER_ADMIN_API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API token")