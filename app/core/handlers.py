from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    CategoryAlreadyExists, CategoryNotFound,
    ProductAlreadyExists, ProductNotFound
)


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


async def product_not_found_handler(
    request: Request,
    exc: ProductNotFound
):

    return JSONResponse(
        status_code=404,
        content={
            "detail": str(exc)
        }
    )


async def product_already_exists_handler(
    request: Request,
    exc: ProductAlreadyExists
):

    return JSONResponse(
        status_code=409,
        content={
            "detail": str(exc)
        }
    )