from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class Stores(BaseModel):
    __tablename__ = "stores"
    store_id = Column(Integer, primary_key=True)
    store_name = Column(String(100))
    store_url = Column(String(100))
    store_description = Column(String(100))
    store_rating = Column(String(100))
    store_contact = Column(String(100))

    def __str__(self):
        return f"""
        Id: {self.store_id}, 
        Name: {self.store_name}, 
        Url: {self.store_url}, 
        Descrição: {self.store_description}, 
        Avaliação: {self.store_rating }, 
        Contato: {self.store_contact}"""
