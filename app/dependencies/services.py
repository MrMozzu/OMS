from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.database import get_db
from app.services.category import CategoryService 


async def provide_category_service(
    session: AsyncSession = Depends(get_db)
) -> CategoryService:

    return CategoryService(session)


