from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM, validator
import re


class UserSQL(BaseModel):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    logins = relationship("LoginSQL", back_populates="user")


class User(BM):
    user_id: int = None
    user_name: str
    email: str
    password: str


class SimpleUser(BM):
    email: str
    password: str

    # @validator("user_name")
    # def validate_username(cls, value):
    #     if len(value) > 255:
    #         raise ValueError("Nome deve ter no máximo 255 caracteres")
    #     return value

    @validator("email")
    def validate_email(cls, value):
        if not re.match("^[a-z0-9@\.]{1,255}$", value):
            raise ValueError("Email no formato invalido")
        return value

    @validator("password")
    def validate_password(cls, value):
        if len(value) > 255:
            raise ValueError("A senha deve ter no máximo 255 caracteres")
        return value
