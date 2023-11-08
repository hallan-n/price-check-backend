from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM


class ProductSQL(BaseModel):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(40))
    description = Column(String(40))
    category = Column(String(40))
    brand = Column(String(40))
    model = Column(String(40))
    price = Column(String(40))
    product_url = Column(String(40))
    update_date = Column(String(40))
    average_rating = Column(String(40))
    availability = Column(String(40))

    store_id = Column(Integer, ForeignKey("stores.store_id"))
    store = relationship("StoreSQL", back_populates="products")

    def __str__(self):
        return f"Id: {self.product_id}, \nNome: {self.product_name}, \nDescrição: {self.description}, \nCategoria: {self.category}, \nMarca: {self.brand}, \nModelo: {self.model}, \nPreço: {self.price}, \nurl: {self.product_url}, \nLoja: {self.store}, \nData de atualização: {self.update_date}, \nAvaliação: {self.average_rating}, \nDisponibilidade: {self.availability}"


class Product(BM):
    product_id: int
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
