from typing import Generic, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("Modeltype")

class BaseRepository(Generic[ModelType]):

    def __init__(self, session: AsyncSession):
        self.session = session
        