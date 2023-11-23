from app.database.connection import get_session
from app.models.base_model import BaseModel, Base
from pydantic import BaseModel as BM
from fastapi import HTTPException
from app.models.store import StoreSQL
from app.models.login import LoginSQL
from app.models.product import ProductSQL
from app.models.user import UserSQL, SimpleUser
import mysql.connector
from mysql.connector.errors import DatabaseError
from dotenv import load_dotenv
import os
from app.services.auth import data_hash, verify_hash

session = get_session()


def create_tables():
    _create_db_mysql()
    Base.metadata.create_all(session.bind)


def verify_user(value: SimpleUser):
    user = session.query(UserSQL).filter(UserSQL.email == value.email).first()
    if user and verify_hash(value.password, user.password):
        return user
    return None


def read_user_for_email(email: str):
    data = session.query(UserSQL).filter(UserSQL.email == email).first()
    if not data:
        return False
    return data


def read(data_tuple: tuple, id: int):
    data = session.query(data_tuple[0]).filter(data_tuple[1] == id).first()
    if not data:
        return False
    return data


def create(value: BM, data_tuple: tuple):
    try:
        if data_tuple[0] == UserSQL:
            if read_user_for_email(value.email):
                return "Email já cadastrado"
            value.password = data_hash(value.password)
        if data_tuple[0] == LoginSQL:
            if read(data_tuple=data_tuple, id=value.login_id):
                return "Login já cadastrado"
            value.password = data_hash(value.password)
        data = dict(value)
        sql_class = data_tuple[0](**data)
        session.add(sql_class)
        session.commit()
        return True
    except:
        session.rollback()
        raise HTTPException(status_code=409, detail="Usuário invalido")
    finally:
        session.close()


def read_all(data_tuple: tuple):
    data = session.query(data_tuple[0]).all()
    if not data:
        return {"message": "Not found"}
    return data


def update(value: BM, data_tuple: tuple, token: str = None):
    try:
        if data_tuple[0] == UserSQL:
            user = read_user_for_email(token)
            if user:
                value.user_id = user.user_id
                value.password = data_hash(value.password)
                data = dict(value)
                session.query(UserSQL).filter(UserSQL.email == token).update(data)
                session.commit()
                session.refresh(user)
        session.close()
        return {"message": "Updated successfully"}
    except:
        return {"message": "Deu ruim"}


# def delete(id: int, schema: str):
#     ClassSQL = _verify_schema(schema)
#     verify = read(id=id,schema=schema)
#     if isinstance(verify, ClassSQL[0]):
#         session.query(ClassSQL[0]).filter(ClassSQL[1] == id).delete()
#         session.commit()
#         return {"message": "Deleted successfully"}
#     return {"message": f"{schema.capitalize()} not found"}


# def read_all(schema: str):
#     ClassSQL = _verify_schema(schema)
#     data = session.query(ClassSQL[0]).all()
#     return data


# def _to_sqlalchemy(value: BM, schema: str):
#     if schema == "user":
#         value.password = data_hash(value.password)
#     sql_data = dict(value)
#     ClassSQL = _verify_schema(schema)[0]
#     return ClassSQL(**sql_data)


# def _get_id(value: [BM | BaseModel]):
#     if isinstance(value, BM):
#         for att in value.__annotations__:
#             if att.endswith("id"):
#                 return getattr(value, att)


# def _verify_schema(schema: str):
#     if schema == "user":
#         return (UserSQL, UserSQL.user_id)
#     if schema == "store":
#         return (StoreSQL, StoreSQL.store_id)
#     if schema == "product":
#         return (ProductSQL, ProductSQL.product_id)
#     if schema == "login":
#         return (LoginSQL, LoginSQL.login_id)


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
