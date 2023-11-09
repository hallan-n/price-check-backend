from fastapi import APIRouter
from app.models.product import Product
from app.database.persistence import create

router = APIRouter(prefix="/product")


@router.post("/register")
async def user_register(user: Product):
    return create(user)
