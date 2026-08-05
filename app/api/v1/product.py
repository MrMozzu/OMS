from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.product import Product
from app.dependencies.database import get_db

from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
    ProductWithCategory
)

from app.services.product import ProductService


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post(
    "", response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(get_db)
):

    service = ProductService(session)

    return await service.create_product(product)


@router.get(
    "/{product_id}", 
    response_model=ProductWithCategory
)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(get_db)
):

    service = ProductService(session)

    return await service.get_product(product_id)


@router.patch(
    "/{product_id}", response_model=ProductResponse
)
async def update_product(
    product_id: int,
    product_data: ProductUpdate,
    session: AsyncSession = Depends(get_db)
):

    service = ProductService(session)

    return await service.update_product(product_id, product_data)


@router.delete(
    "/{product_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(get_db)
):

    service = ProductService(session)

    return await service.delete_product(product_id)