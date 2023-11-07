from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel


class LoginSQL(BaseModel):
    __tablename__ = "logins"
    login_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)

    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("UserSQL", back_populates="logins")

    def __str__(self):
        return (
            f"Id: {self.login_id}, \nUsuário: {self.username}, \nSenha: {self.password}"
        )
