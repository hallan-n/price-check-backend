from fastapi import APIRouter
from app.models.store import Store
from app.database.persistence import create

router = APIRouter(prefix="/store")


@router.post("/register")
async def user_register(user: Store):
    return create(user)
