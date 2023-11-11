from fastapi import APIRouter
from app.models.product import Product
from app.database.persistence import create, delete, read, update, read_all

router = APIRouter()


@router.get("/product/{id}")
async def get_product(id: int):
    """Pega um produto com base no ID"""
    resp = read(id, "product")
    return resp


@router.get("/product")
async def get_all_product():
    """Pega um produto com base no ID"""
    resp = read_all("product")
    return resp


@router.post("/product")
async def create_product(product: Product):
    """Cria um produto"""
    resp = create(product, "product")
    return resp


@router.delete("/product/{id}")
async def delete_product(id: int):
    """Delete um produto com base no ID"""
    resp = delete(id, "product")
    return resp


@router.put("/product")
async def update_product(product: Product):
    """Atualiza um produto"""
    resp = update(product, "product")
    return resp
