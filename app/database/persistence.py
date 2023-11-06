from app.database.connection import get_session
from app.models.users import User
from app.models.base_model import BaseModel, Base

session = get_session()

Base.metadata.create_all(session.bind)


def create(value: BaseModel):
    session.add(value)
    session.commit()
    session.close()


def delete(idx):
    user = session.query(User).filter(User.id == idx).first()
    session.delete(user)
    session.commit()
    session.close()
