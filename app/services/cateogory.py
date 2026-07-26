from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSessiony

from app.db.models.cateogory import Cateogory
from app.repositories.cateogory import CateogoryRepository


class CateogoryService:

    def __init__(
        self,
        session: AsyncSession
    ):

        self.repository = CateogoryRepository(session)
        self.session = session
        
    
    async def create_cateorgory(
        self,
        name: str
    ) -> Cateogory:

        exists = await self.repository.get_by_name(name)

        if exists:
            raise ValueError(
                "Cateogory already exists"
            )

        cateogory = Cateogory(
            name=name
        )
        
        try:
            await self.repository.create(cateogory)
            await self.session.commit()
            return cateogory

        except Exception:
            await self.session.rollback()
            raise

    
    async def get_cateogory(
        self,
        id: int
    ) -> Cateogory | None:

        cateogory = await self.repository.get_by_id(id)

        if cateogory:
            return cateogory
        
        else:
            raise ValueError(
                "Catogory not exists"
            )

       
