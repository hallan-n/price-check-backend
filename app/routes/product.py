from app.services.auth import decode_token
from fastapi import Depends
from fastapi import APIRouter
from app.models.product import Product, ProductSQL
from app.database.persistence import read, read_all

router = APIRouter()
tuple_product = (ProductSQL, ProductSQL.product_id)


@router.get("/product/{id}")
async def get_product(id: int, token: dict = Depends(decode_token)):
    """Pega um produto com base no ID"""
    resp = read(data_tuple=tuple_product, id=id)
    return resp


@router.get("/product")
async def get_all_product(token: dict = Depends(decode_token)):
    """Pega todos os produtos"""
    resp = read_all(tuple_product)
    return resp


# @router.post("/product")
# async def create_product(product: Product):
#     """Cria um produto"""
#     resp = create(product, "product")
#     return resp


# @router.delete("/product/{id}")
# async def delete_product(id: int):
#     """Delete um produto com base no ID"""
#     resp = delete(id, "product")
#     return resp


# @router.put("/product")
# async def update_product(product: Product):
#     """Atualiza um produto"""
#     resp = update(product, "product")
#     return resp
