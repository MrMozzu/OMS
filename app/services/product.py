from sqlalchemy.exe.asyncio import AsyncSession


from app.db.models.product import Product
from app.repositories.category import CategoryRepository
from app.repositories.product import ProductRepository


class ProductService:

    def __init__(
        self,
        session: AsyncSession
    ):

        self.session = session

        self.product_repository = ProductRepository(session)

        self.category_repository = CategoryRepository(session) 

