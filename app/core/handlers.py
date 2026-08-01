from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import CategoryAlreadyExists, CategoryNotFound


async def category_not_found_handler(
    request: Request,
    exc: CategoryNotFound
):

    return JSONResponse(
        status_code=404,
        content={
            "detail": str(exc)
        }
    )


async def category_already_exists_handler(
    request: Request,
    exc: CategoryAlreadyExists
):

    return JSONResponse(
        status_code=409,
        content={
            "detail": str(exc)
        }
    )