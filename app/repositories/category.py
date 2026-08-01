from sqlalchemy import select

from app.db.models.category import Category
from app.repositories.base import BaseRepository



class CategoryRepository(
    BaseRepository[Category]
):

    async def get_by_id(
        self,
        category_id: int,
    ) -> Category | None:

        stmt = (
            select(Category)
            .where(Category.id == category_id)
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()


    async def get_by_name(
        self, 
        name: str
    ) -> Category | None:

        stmt = (
            select(Category)
            .where(Category.name == name)
        )
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()


    async def create(
        self, 
        category: Category,
    ) -> Category:
        
        self.session.add(category)

        await self.session.flush()
        await self.session.refresh(category)

        return category


    async def delete(
        self,
        category: Category
    ) -> None:
        
        await self.session.delete(category)
        await self.session.flush()
