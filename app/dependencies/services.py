from fastapi import Depends
from sqlalchemy.exe.asyncio import AsyncSession

from app.dependencies.database import get_db
from app.services.category import CategoryService 


async def get_category_service(
    session: AsyncSession = Depends(get_db)
) -> CategoryService:

    return CategoryService(session)