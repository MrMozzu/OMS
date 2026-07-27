from app.db.models.category import Category
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(nullable=False)

    stock: Mapped[int] 

    price: Mapped[float]

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        back_populates="products"
    )

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="product"
    )