from pydantic import BaseModel, ConfigDict, Field

class CategoryCreate(BaseModel):
    
    name: str = Field(
        min_length=3,
        max_length=40
    )


class CategoryUpdate(BaseModel):

        name: str | None = Field(
            default=None,
            min_length=2,
            max_length=40
        )


class CategoryResponse(BaseModel):

    model_config = ConfigDict(
       from_attributes=True
    )

    id: int
    name: str
    

class CategorySimple(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    name: str
