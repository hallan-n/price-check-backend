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
    sql_class = _normilize(value, schema)
    session.add(sql_class)
    session.commit()
    session.close()
    return "criado"


def _normilize(value: BM, schema: str) -> BaseModel:
    if schema == "user":
        user = UserSQL(
            user_id=value.user_id,
            user_name=value.user_name,
            email=value.email,
            password=value.password,
        )
        return user
    if schema == "store":
        store = StoreSQL(
            store_id=schema.store_id,
            store_name=schema.store_name,
            store_url=schema.store_url,
            store_description=schema.store_description,
            store_rating=schema.store_rating,
            store_contact=schema.store_contact,
        )
        return store
    if schema == "product":
        product = ProductSQL(
            product_id=schema.product_id,
            product_name=schema.product_name,
            description=schema.description,
            category=schema.category,
            brand=schema.brand,
            model=schema.model,
            price=schema.price,
            product_url=schema.product_url,
            update_date=schema.update_date,
            average_rating=schema.average_rating,
            availability=schema.availability,
            store_id=schema.store_id,
        )
        return product
    if schema == "login":
        login = LoginSQL(
            login_id=schema.login_id,
            username=schema.username,
            password=schema.password,
            user_id=schema.user_id,
        )
        return login


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
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_DATABASE')};")
    except DatabaseError as e:
        print(">>>>>>", e.msg)
