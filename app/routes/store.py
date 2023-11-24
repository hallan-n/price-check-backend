from app.services.auth import decode_token
from fastapi import Depends
from fastapi import APIRouter
from app.models.store import StoreSQL
from app.database.persistence import read_all, read

router = APIRouter()
tuple_store = (StoreSQL, StoreSQL.store_id)


@router.get("/store")
async def get_all_stores(token: dict = Depends(decode_token)):
    """Pega todas as lojas"""
    resp = read_all(tuple_store)
    return resp


@router.get("/store/{id}")
async def get_tore(id: int, token: dict = Depends(decode_token)):
    """Pega todas as lojas"""
    resp = read(data_tuple=tuple_store, id=id)
    return resp
