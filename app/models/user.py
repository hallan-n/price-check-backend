from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
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

    
    # @validates("user_name")
    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise ValueError("O campo 'name' deve conter pelo menos 3 caracteres.")
    #     return value

    # @validator("user_name")
    # def validate_username(cls, value):
    #     if not re.match("^[a-z0-9@]{1,255}$", value):
    #         raise ValueError("Username format invalid")
    #     return value
