from app.database.connection import get_session
from app.models.base_model import BaseModel, Base

from app.models.store import StoreSQL
from app.models.login import LoginSQL
from app.models.product import ProductSQL
from app.models.user import UserSQL

import mysql.connector
from mysql.connector.errors import DatabaseError
from dotenv import load_dotenv
import os

session = get_session()


def create_tables():
    _create_db_mysql()
    Base.metadata.create_all(session.bind)


def _create_db_mysql():
    load_dotenv()
    conn = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
    }

    try:
        mydb = mysql.connector.connect(**conn)
        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE {os.getenv('DB_DATABASE')};")
        print("O banco foi criado")
    except DatabaseError as e:
        print(">>>>>>", e.msg)


# def create(value: BaseModel):
#     session.add(value)
#     session.commit()
#     session.close()


# def delete(idx):
#     user = session.query(User).filter(User.id == idx).first()
#     session.delete(user)
#     session.commit()
#     session.close()
