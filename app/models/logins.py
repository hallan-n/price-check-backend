from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel


class Login(BaseModel):
    __tablename__ = "logins"
    login_id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))

    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("User", back_populates="logins")

    def __str__(self):
        return f"""
        Id: {self.login_id}, 
        Usuário: {self.username}, 
        Senha: {self.password}  
        """
