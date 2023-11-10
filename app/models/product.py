from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM


class ProductSQL(BaseModel):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    product_name = Column(String(255))
    description = Column(String(255))
    category = Column(String(255))
    brand = Column(String(255))
    model = Column(String(255))
    price = Column(String(255))
    product_url = Column(String(255))
    update_date = Column(String(255))
    average_rating = Column(String(40))
    availability = Column(String(40))
    store_id = Column(Integer, ForeignKey("stores.store_id"))
    store = relationship("StoreSQL", back_populates="products")


class Product(BM):
    product_id: int = None
    product_name: str
    description: str
    category: str
    brand: str
    model: str
    price: str
    product_url: str
    update_date: str
    average_rating: str
    availability: str
    store_id: int = None
