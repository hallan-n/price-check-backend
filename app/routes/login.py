from fastapi import APIRouter
from app.models.login import Login
from app.database.persistence import create

router = APIRouter()


@router.post("/login")
async def user_register(login: Login):
    resp = create(login, "login")
    return resp


# @router.get("/user/{id}")
# async def get_user(id: int):
#     return create("login", "login")
