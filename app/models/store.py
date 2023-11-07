from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel


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
