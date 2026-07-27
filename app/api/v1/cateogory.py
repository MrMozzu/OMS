from fastapi import Depends
from sqlalchemy.exe.asyncio import AsyncSession

from app.dependencies.services import get_category_service
from app.schemas.category import CategoryCreate, CategoryResponse

from app.services.category import CategoryService


@router.post("/",
    reponse_model=CategoryResponse,
    status_code=201    
)

async def create_category(
    data: CategoryCreate,
    service: CategoryService = Depends(
        get_category_service
    )
):

    return await service.create_category(data)

    