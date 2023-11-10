from fastapi import APIRouter
from app.models.product import Product
from app.database.persistence import create

router = APIRouter()


@router.post("/product")
async def user_register(user: Product):
    return create(user)
