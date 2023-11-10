from app.database.connection import get_session
from app.models.base_model import BaseModel, Base
from pydantic import BaseModel as BM
from app.models.store import StoreSQL
from app.models.login import LoginSQL
from app.models.product import ProductSQL
from app.models.user import UserSQL, User

import mysql.connector
from mysql.connector.errors import DatabaseError
from dotenv import load_dotenv
import os

session = get_session()


def create_tables():
    _create_db_mysql()
    Base.metadata.create_all(session.bind)


def create(value: BM, schema: str):
    sql_class = _to_sqlalchemy(value=value, schema=schema)
    session.add(sql_class)
    session.commit()
    session.close()
    return {"message": "User created successfully"}


# Método para atualizar um usuário por ID
def update(id: int, data: BM):
    session.query(BM).filter(UserSQL.user_id == id).update(data)
    session.commit()
    return {"message": "User updated successfully"}


def delete(id: int, schema: str):
    ClassSQL = _verify_schema(schema)
    session.query(ClassSQL[0]).filter(ClassSQL[1] == id).delete()
    session.commit()
    return {"message": "User deleted successfully"}


def read(id: int, schema: str):
    return session.query(UserSQL).filter(UserSQL.user_id == id).first()


def _verify_schema(schema: str):
    if schema == "user":
        return (UserSQL, UserSQL.user_id)
    if schema == "store":
        return (StoreSQL, StoreSQL.store_id)
    if schema == "product":
        return (ProductSQL, ProductSQL.product_id)
    if schema == "login":
        return (LoginSQL, LoginSQL.login_id)


def _to_sqlalchemy(value: BM, schema: str):
    sql_data = dict(value)
    if schema == "user":
        user = UserSQL(**sql_data)
        return user
    if schema == "store":
        store = StoreSQL(**sql_data)
        return store
    if schema == "product":
        product = ProductSQL(**sql_data)
        return product
    if schema == "login":
        login = LoginSQL(**sql_data)
        return login


def _create_db_mysql():
    load_dotenv()
    try:
        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_DATABASE')};")
    except DatabaseError as e:
        print(">>>>>>", e.msg)
