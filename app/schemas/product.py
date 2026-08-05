from decimal import Decimal 

from pydantic import ConfigDict, BaseModel
from app.schemas.category import CategorySimple



class ProductCreate(BaseModel):

    name: str

    price: Decimal 

    stock: int

    category_id: int



class ProductUpdate(BaseModel):

    name: str | None = None

    description: str | None = None

    price: int | None = None

    stock: int | None = None



class ProductResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )


    id: int

    name: str

    description: str | None = None

    price: Decimal

    stock: int

    category_id: int


class ProductWithCategory(ProductResponse):

    category: CategorySimple