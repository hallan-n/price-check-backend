from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM


class ProductSQL(BaseModel):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    product_name = Column(String(600), nullable=True)
    description = Column(String(600), nullable=True)
    category = Column(String(600), nullable=True)
    brand = Column(String(600), nullable=True)
    model = Column(String(600), nullable=True)
    price = Column(String(600), nullable=True)
    product_url = Column(String(600), nullable=True)
    average_rating = Column(String(600), nullable=True)
    availability = Column(String(600), nullable=True)
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
    average_rating: str = None
    availability: str = None
    store_id: int = None
