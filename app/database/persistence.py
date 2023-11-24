from app.database.connection import get_session
from app.models.base_model import BaseModel, Base
from app.services.decorators import run_once
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
from functools import lru_cache

session = get_session()

@run_once
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


def read_login_for_id(store_id: int, user_id: int):
    try:
        data = session.query(LoginSQL).filter(LoginSQL.store_id == store_id, LoginSQL.user_id == user_id).first()
        return data
    except:
            return False

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



@lru_cache(maxsize=None)
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
        return {"message": "Não foi possível atualizar"}


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
