from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import CategoryAlreadyExists, CategoryNotFound
from app.db.models.category import Category
from app.repositories.category import CategoryRepository


class CategoryService:

    def __init__(
        self,
        session: AsyncSession
    ):

        self.repository = CategoryRepository(session)
        self.session = session
        
    
    async def create_category(
        self,
        name: str
    ) -> Category:

        exists = await self.repository.get_by_name(name)

        if exists:
            raise CategoryAlreadyExists()
            
        category = Category(
            name=name
        )
        
        try:
            await self.repository.create(category)
            await self.session.commit()
            return category

        except Exception:
            await self.session.rollback()
            raise

    
    async def get_category(
        self,
        category_id: int
    ) -> Category:

        category = await self.repository.get_by_id(category_id)

        if category:
            return category
        
        else:
            raise CategoryNotFound()

       
    async def update_category(
        self, 
        category_id: int,
        name: str
    ) -> Category:

        category = await self.get_category(category_id)

        existing = await self.repository.get_by_name(name)

        if (
            existing and 
            existing.id != category.id
        ):
            raise CategoryAlreadyExists()

        category.name = name

        try: 
            await self.session.commit()
            await self.session.refresh(category)
            return category
        
        except Exception:

            await self.session.rollback()
            raise

   
    async def delete_category(
        self,
        category_id: int
    ) -> None:

        category = await self.repository.get_by_id(category_id)

        if not category:
            raise CategoryNotFound()
        
        await self.repository.delete(category)

        try:
            await self.session.commit()

        except Exception:
            await self.session.rollback()
            raise 


        