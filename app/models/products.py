from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel


class Stores(BaseModel):
    __tablename__ = "users"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(100))
    description = Column(String(100))
    category = Column(String(100))
    brand = Column(String(100))
    model = Column(String(100))
    price = Column(String(100))
    product_url = Column(String(100))
    store = Column(String(100))
    update_date = Column(String(100))
    average_rating = Column(String(100))
    availability = Column(String(100))

    def __str__(self):
        return f"""
        Id: {self.product_id}, 
        Nome: {self.product_name}, 
        Descrição: {self.description}, 
        Categoria: {self.category}, 
        Marca: {self.brand}, 
        Modelo: {self.model}, 
        Preço: {self.price}, 
        url: {self.product_url}, 
        Loja: {self.store}, 
        Data de atualização: {self.update_date}, 
        Avaliação: {self.average_rating}, 
        Disponibilidade: {self.availability}"""
