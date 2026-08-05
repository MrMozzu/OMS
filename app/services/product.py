from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import (
    CategoryNotFound,
    ProductAlreadyExists,
    ProductNotFound,
)
from app.db.models.product import Product
from app.repositories.category import CategoryRepository
from app.repositories.product import ProductRepository
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate


class ProductService:

    def __init__(
        self,
        session: AsyncSession
    ):

        self.session = session

        self.product_repository = ProductRepository(session)

        self.category_repository = CategoryRepository(session) 



    async def create_product(
        self,
        product_data: ProductCreate
    ) -> Product:

        if product_data.price <= 0:
            raise ValueError(
                "Price must be greater than zero"
            )
        
        if product_data.stock < 0:
            raise ValueError(
                "Stock must be positive"
            )

        category = await self.category_repository.get_by_id(
            product_data.category_id
        )
         
        if category is None:
            raise CategoryNotFound()

        existing_product = await self.product_repository.get_by_name(
            product_data.name
        )
        if existing_product:
            raise ProductAlreadyExists()

        product = Product(
            name=product_data.name,
            price=product_data.price,
            stock=product_data.stock,
            category_id=product_data.category_id
        )
        
        try:
            await self.product_repository.create(product)
            await self.session.commit()
            return product

        except Exception:
            await self.session.rollback()
            raise


    async def get_product(
        self,
        product_id: int
    ) -> Product:

        product = await self.product_repository.get_with_category(product_id)

        if product is None:
            raise ProductNotFound()
        
        return product


    async def get_all(
        self
    ) -> list[Product]:

        products = await self.product_repository.get_all()

        return products

    
    async def update_product(
        self,
        product_id: int,
        product_data: ProductUpdate
    ) -> Product:

        product = await self.get_product(product_id)

        if product_data.name is not None:
            product.name = product_data.name
        if product_data.price is not None:
            product.price = product_data.price
        if product_data.stock is not None:
            product.stock = product_data.stock

        try:
            await self.product_repository.update(product)
            await self.session.commit()
            return product
        except Exception:
            await self.session.rollback()
            raise


    async def delete_product(
        self,
        product_id: int
    ) -> None:

        product = await self.get_product(product_id)

        await self.product_repository.delete(product)

        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
