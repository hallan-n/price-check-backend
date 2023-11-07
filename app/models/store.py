from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from app.models.product import ProductSQL
from pydantic import BaseModel as BM
from typing import List


class StoreSQL(BaseModel):
    __tablename__ = "stores"
    store_id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String)
    store_url = Column(String)
    store_description = Column(String)
    store_rating = Column(String)

    store_contact = Column(String)
    products = relationship("ProductSQL", back_populates="store")

    def __str__(self):
        return f"Id: {self.store_id}, \nName: {self.store_name}, \nUrl: {self.store_url}, \nDescrição: {self.store_description}, \nAvaliação: {self.store_rating }, \nContato: {self.store_contact}"


class Store(BM):
    store_id: int
    store_name: str
    store_url: str
    store_description: str
    store_rating: str
    store_contact: str
    products: List[ProductSQL]
