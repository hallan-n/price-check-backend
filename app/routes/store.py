from fastapi import APIRouter
from app.models.store import Store
from app.database.persistence import create, delete, read, update, read_all

router = APIRouter()


@router.get("/store/{id}")
async def get_store(id: int):
    """Pega uma loja com base no ID"""
    resp = read(id, "store")
    return resp


@router.get("/store")
async def get_all_store():
    """Pega uma loja com base no ID"""
    resp = read_all("store")
    return resp


@router.post("/store")
async def create_store(store: Store):
    """Cria uma loja"""
    resp = create(store, "store")
    return resp


@router.delete("/store/{id}")
async def delete_store(id: int):
    """Delete uma loja com base no ID"""
    resp = delete(id, "store")
    return resp


@router.put("/store")
async def update_store(store: Store):
    """Atualiza uma loja"""
    resp = update(store, "store")
    return resp
