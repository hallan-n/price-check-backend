from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM


class StoreSQL(BaseModel):
    __tablename__ = "stores"
    store_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    store_name = Column(String(400), nullable=True)
    store_url = Column(String(400), nullable=True)
    store_description = Column(String(400), nullable=True)
    store_rating = Column(String(400), nullable=True)
    products = relationship("ProductSQL", back_populates="store")
    login = relationship("LoginSQL", back_populates="store")


class Store(BM):
    store_id: int = None
    store_name: str = None
    store_url: str = None
    store_description: str = None
    store_rating: str = None
