from fastapi import APIRouter, HTTPException
from app.config import server
from tracardi.config import tracardi

router = APIRouter()


@router.get("/info/version", tags=["info"], include_in_schema=server.expose_gui_api, response_model=str)
async def get_version():
    return tracardi.version

