from fastapi import APIRouter
from app.models.user import User
from app.database.persistence import create

router = APIRouter(prefix="/user")


@router.post("/register")
async def user_register(user: User):
    return create(user, "user")
