from fastapi import APIRouter
from app.models.store import Store
from app.database.persistence import create

router = APIRouter()


@router.post("/store")
async def user_register(user: Store):
    return create(user)
