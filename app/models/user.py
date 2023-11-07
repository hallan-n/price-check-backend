from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel


class UserSQL(BaseModel):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
    logins = relationship("LoginSQL", back_populates="user")

    def __str__(self):
        return f"Id: {self.user_id}, \nNome: {self.user_name}, \nIdade: {self.email}, \nPassword: {self.password}, \nLogins: {self.logins}"
