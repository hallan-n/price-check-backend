from fastapi import APIRouter
from app.models.login import Login
from app.database.persistence import create

router = APIRouter(prefix="/login")


@router.post("/register")
async def user_register(login: Login):
    return create(login, "login")
