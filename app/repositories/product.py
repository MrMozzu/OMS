from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.models.product import Product 
from app.repositories.base import BaseRepository


class ProductRepository(
    BaseRepository[Product]
):


    async def create(
        self,
        product: Product
    ) -> Product:

        self.session.add(product)

        await self.session.flush()

        await self.session.refresh(product)

        return product 
    

    async def get_by_id(
        self,
        product_id:  int
    ) -> Product | None:

        statement = (
            select(Product)
            .where(Product.id == product_id)
        )

        result = await self.session.execute(statement)

        return result.scalar_one_or_none()

    
    async def get_by_name(
        self,
        product_name: str
    ) -> Product:

        statement = (
            select(Product)
            .where(Product.name == product_name)
        )

        result = await self.session.execute(statement)

        return result.scalar_one_or_none()


    async def get_with_category(
        self,
        product_id: int
    ) -> Product | None:

        statement = (
            select(Product)
            .options(selectinload(Product.category)) # to get the related categories
            .where(Product.id == product_id)
        )

        result = await self.session.execute(statement)

        return result.scalar_one_or_none()



    async def get_all(
        self,
    ) -> list[Product]:

        statement = select(Product)

        result = await self.session.execute(statement)

        return list(result.scalar().all())

    
    async def update(
        self,
        product: Product
    ) -> Product:

        await self.session.flush()
        await self.session.refresh(product)
        return product


    async def delete(
            self,
            product: Product
        ) -> None:
        
        await self.session.delete(product)
