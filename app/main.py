from fastapi import FastAPI

from app.api.v1.category import router as category_router

from app.core.exceptions import CategoryAlreadyExists, CategoryNotFound
from app.core.handlers import category_already_exists_handler, category_not_found_handler

app = FastAPI(title="Order Management System API")


app.add_exception_handler(
    CategoryNotFound,
    category_not_found_handler
)

app.add_exception_handler(
    CategoryAlreadyExists,
    category_already_exists_handler
)

app.include_router(category_router, prefix="/api/v1")