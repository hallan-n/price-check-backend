# from app.database.persistence import create_tables
# from app.database.persistence import create
# from app.models.user import User

from fastapi import FastAPI
from app.routes.user import router

app = FastAPI()
app.include_router(router)

# create_tables()
# u1 = User(user_name="asd",email="asd",password="asd")
# create(u1)