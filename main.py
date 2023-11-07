# from fastapi import FastAPI
# from app.routes.teste import router

# app = FastAPI()
# app.include_router(router)

from app.database.persistence import create
from app.models.users import User

u1 = User(user_name="asd",email="asd",password="asd")
print(u1)
create(u1)