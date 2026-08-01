from fastapi import Depends, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.services import provide_category_service
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate

from app.services.category import CategoryService


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post("/",
    response_model=CategoryResponse,
    status_code=201    
)
async def create_category(
    data: CategoryCreate,
    service: CategoryService = Depends(
        provide_category_service
    )
):

    return await service.create_category(data.name)


    
@router.get(
    "/{category_id}",
    response_model=CategoryResponse
)
async def get_category(
    category_id: int,
    service: CategoryService = Depends(
        provide_category_service
    )
):

    return await service.get_category(category_id)



@router.patch(
    "/{category_id}",
    response_model=CategoryResponse
)
async def update_category(
    category_id: int,
    data: CategoryUpdate,
    service: CategoryService = Depends(
        provide_category_service
    )
):

    return await service.update_category(category_id, data.name)


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_200_OK
)
async def delete_category(
    category_id: int,
    service: CategoryService = Depends(
        provide_category_service
    )
):

    await service.delete_category(category_id)
    return {"message": "Category deleted successfully"}