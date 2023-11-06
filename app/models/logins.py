from sqlalchemy import Column, Integer, String
from app.models.base_model import BaseModel


class Login(BaseModel):
    __tablename__ = "logins"
    login_id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))
    store = Column(String(100))


    """
    # Chave estrangeira para a tabela de Usuários
    user_id = Column(Integer, ForeignKey('usuarios.id'))

    # Relação com a tabela de Usuários
    usuario = relationship('Usuario', back_populates='logins')
    """

    def __str__(self):
        return f"Id: {self.login_id}, Username: {self.username}, Password: {self.password}, Store: {self.store}"
