from app.database.connection import get_session
from app.models.base_model import BaseModel, Base
from pydantic import BaseModel as BM
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


def create(value: BM, schema: str):
    try:
        sql_class = _to_sqlalchemy(value, schema)
        session.add(sql_class)
        session.commit()
    except Exception as e:
        print(f"Erro ao tentar inserir {e}")
        session.rollback()
    finally:
        session.close()

    return {"message": "Created successfully"}


def update(value: BM, schema: str):
    data = dict(value)
    ClassSQL = _verify_schema(schema)
    id = _get_id(value)
    session.query(ClassSQL[0]).filter(ClassSQL[1] == id).update(data)
    session.commit()
    return {"message": "Updated successfully"}


def delete(id: int, schema: str):
    ClassSQL = _verify_schema(schema)
    session.query(ClassSQL[0]).filter(ClassSQL[1] == id).delete()
    session.commit()
    return {"message": "Deleted successfully"}


def read(id: int, schema: str):
    ClassSQL = _verify_schema(schema)
    data = session.query(ClassSQL[0]).filter(ClassSQL[1] == id).first()
    if not data:
        return {"message": "Not found"}
    return data


def read_all(schema: str):
    ClassSQL = _verify_schema(schema)
    data = session.query(ClassSQL[0]).all()
    return data


def _to_sqlalchemy(value: BM, schema: str):
    sql_data = dict(value)
    ClassSQL = _verify_schema(schema)[0]
    return ClassSQL(**sql_data)


def _get_id(value: [BM | BaseModel]):
    if isinstance(value, BM):
        for att in value.__annotations__:
            if att.endswith("id"):
                return getattr(value, att)


def _verify_schema(schema: str):
    if schema == "user":
        return (UserSQL, UserSQL.user_id)
    if schema == "store":
        return (StoreSQL, StoreSQL.store_id)
    if schema == "product":
        return (ProductSQL, ProductSQL.product_id)
    if schema == "login":
        return (LoginSQL, LoginSQL.login_id)


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
