from fastapi import APIRouter
from app.models.login import Login
from app.database.persistence import create, delete, read, update, read_all

router = APIRouter()


@router.get("/login/{id}")
async def get_product(id: int):
    """Pega um login com base no ID"""
    resp = read(id, "login")
    return resp


@router.get("/login")
async def get_all_product():
    """Pega todos os logins"""
    resp = read_all("product")
    return resp


@router.post("/login")
async def create_product(login: Login):
    """Cria um login"""
    resp = create(login, "login")
    return resp


@router.delete("/login/{id}")
async def delete_product(id: int):
    """Delete um login com base no ID"""
    resp = delete(id, "login")
    return resp


@router.put("/login")
async def update_product(login: Login):
    """Atualiza um login"""
    resp = update(login, "login")
    return resp
