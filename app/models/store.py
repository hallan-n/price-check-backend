from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM


class StoreSQL(BaseModel):
    __tablename__ = "stores"
    store_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    store_name = Column(String(255))
    store_url = Column(String(255))
    store_description = Column(String(255))
    store_rating = Column(String(40))
    store_contact = Column(String(40))
    login_id = Column(Integer, ForeignKey("logins.login_id"))
    products = relationship("ProductSQL", back_populates="store")
    login = relationship("LoginSQL", back_populates="store")


class Store(BM):
    store_id: int = None
    store_name: str
    store_url: str
    store_description: str
    store_rating: str
    store_contact: str
