from app.database.connection import get_session
from app.models.base_model import BaseModel, Base

from app.models.store import StoreSQL
from app.models.login import LoginSQL
from app.models.product import ProductSQL
from app.models.user import UserSQL


session = get_session()


def create_tables():
    Base.metadata.create_all(session.bind)


# def create(value: BaseModel):
#     session.add(value)
#     session.commit()
#     session.close()


# def delete(idx):
#     user = session.query(User).filter(User.id == idx).first()
#     session.delete(user)
#     session.commit()
#     session.close()
