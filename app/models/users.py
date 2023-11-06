from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100))
    email = Column(String(255))
    password = Column(String(60))
    #                  classe de relação
    logins = relationship('Login', back_populates='usuario')


    def __str__(self):
        return f"Id: {self.id}, Nome: {self.nome}, Idade: {self.email}, Password: {self.password}"
