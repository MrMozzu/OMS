from fastapi import FastAPI

from app.api.v1.category import router as category_router
from app.api.v1.product import router as product_router

import app.db.models  # Register all SQLAlchemy models

from app.core.exceptions import (
    CategoryAlreadyExists, CategoryNotFound,
    ProductAlreadyExists, ProductNotFound
)
from app.core.handlers import (
    category_already_exists_handler, category_not_found_handler,
    product_already_exists_handler, product_not_found_handler
)

app = FastAPI(title="Order Management System API")


app.add_exception_handler(
    CategoryNotFound,
    category_not_found_handler
)

app.add_exception_handler(
    CategoryAlreadyExists,
    category_already_exists_handler
)

app.add_exception_handler(
    ProductNotFound,
    product_not_found_handler
)

app.add_exception_handler(
    ProductAlreadyExists,
    product_already_exists_handler
)

app.include_router(category_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1")

