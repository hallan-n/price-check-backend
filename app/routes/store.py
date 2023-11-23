from app.services.auth import decode_token
from fastapi import Depends
from fastapi import APIRouter
from app.models.store import StoreSQL
from app.database.persistence import read_all

router = APIRouter()
tuple_store = (StoreSQL, StoreSQL.store_id)


@router.get("/store")
async def get_store(token: dict = Depends(decode_token)):
    """Pega todas as lojas"""
    resp = read_all(tuple_store)
    return resp
