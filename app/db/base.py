from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


from app.db.models.category import Category
from app.db.models.product import Product
from app.db.models.order_item import OrderItem
from app.db.models.order import Order

