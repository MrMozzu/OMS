from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.db.base import Base


class Cateogory(Base):
    __tablename__ = "cateogories"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    products: Mapped[list["Product"]] = relationship(
        back_populates="cateogory",
        cascade="all, delete-orphan"
    )


