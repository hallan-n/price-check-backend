from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM, validator
import re


class UserSQL(BaseModel):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(40))
    email = Column(String(40))
    password = Column(String(255))
    logins = relationship("LoginSQL", back_populates="user")

    # @validates("user_name")
    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise ValueError("O campo 'name' deve conter pelo menos 3 caracteres.")
    #     return value

    # @validates("email")
    # def validate_email(self, value):
    #     if "@" not in value:
    #         raise ValueError("O campo 'email' deve ser um endereço de e-mail válido.")
    #     return value

    # @validates("password")
    # def validate_password(self, value):
    #     if len(value) < 8:
    #         raise ValueError("A senha deve conter pelo menos 8 caracteres.")
    #     return value



class User(BM):
    user_id: int = None
    user_name: str
    email: str
    password: str
    logins: str = None

    @validator("user_name")
    def validate_username(cls, value):
        if not re.match("^[a-z0-9@]{1,255}$", value):
            raise ValueError("Username format invalid")
        return value
