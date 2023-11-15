from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from pydantic import BaseModel as BM


class LoginSQL(BaseModel):
    __tablename__ = "logins"
    login_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(String(255))
    password = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("UserSQL", back_populates="logins")
    store = relationship("StoreSQL", back_populates="login", uselist=False)
    store_id = Column(Integer, ForeignKey("stores.store_id"))

class Login(BM):
    login_id: int = None
    username: str
    password: str
    user_id: int = None
    store_id: int = None