from typing import Optional

from fastapi import APIRouter, Depends
from fastapi import HTTPException

from app.api.auth.authentication import get_current_user
from app.config import server
from tracardi.service.storage.driver import storage

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.get("/instances/page/{page}", tags=["api-instance"], include_in_schema=server.expose_gui_api)
@router.get("/instances", tags=["api-instance"], include_in_schema=server.expose_gui_api)
async def all_api_instances(page: Optional[int] = None):
    try:
        if page is None:
            page = 0
            page_size = 100
        else:
            page_size = server.page_size
        start = page * page_size
        limit = page_size
        result = await storage.driver.api_instance.load_all(start, limit)

        return {
            "total": result.total,
            "result": list(result)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/instances/stale", tags=["api-instance"], include_in_schema=server.expose_gui_api)
async def remove_stale_api_instances():
    """Not implemented"""
    # todo remove stale instances
    pass
