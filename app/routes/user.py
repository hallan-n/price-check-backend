from fastapi import APIRouter
from app.models.user import User
from app.database.persistence import create

router = APIRouter()


@router.post("/user")
async def user_register(user: User):
    resp = create(user, "user")
    return resp
