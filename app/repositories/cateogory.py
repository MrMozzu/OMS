from sqlalchemy import select

from app.db.models.cateogory import Cateogory
from app.repositories.base import BaseRepository

class CateogoryRepository(
    BaseRepository[Cateogory]
):

    async def get_by_id(
        self,
        cateogory_id: int,
    ) -> Cateogory | None:

        stmt = (
            select(Cateogory)
            .where(Cateogory.id == cateogory_id)
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()


    async def get_by_name(
        self, 
        name: str
    ) -> Cateogory | None:

        stmt = (
            select(Cateogory)
            .where(Cateogory.name == name)
        )
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()


    async def create(
        self, 
        cateogory: Cateogory,
    ) -> Cateogory:
        
        self.session.add(cateogory)

        await self.session.flush()
        await self.session.refresh(cateogory)

        return cateogory


    async def delete(
        self,
        cateogory: Cateogory
    ) -> None:
        
        await self.session.delete(cateogory)
        await self.session.flush()
        
    
    