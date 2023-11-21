from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM


class ProductSQL(BaseModel):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    product_name = Column(String(255))
    description = Column(String(400), nullable=True)
    category = Column(String(255), nullable=True)
    brand = Column(String(255), nullable=True)
    model = Column(String(255), nullable=True)
    price = Column(String(255), nullable=True)
    product_url = Column(String(255), nullable=True)
    average_rating = Column(String(40), nullable=True)
    availability = Column(String(40), nullable=True)
    store_id = Column(Integer, ForeignKey("stores.store_id"))
    store = relationship("StoreSQL", back_populates="products")


class Product(BM):
    product_id: int = None
    product_name: str = None
    description: str = None
    category: str = None
    brand: str = None
    model: str = None
    price: str = None
    product_url: str = None
    update_date: str = None
    average_rating: str = None
    availability: str = None
    store_id: int = None
