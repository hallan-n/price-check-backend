from fastapi import APIRouter
from app.models.user import User
from app.database.persistence import create, delete, read, update

router = APIRouter()


@router.get("/user/{id}")
async def get_user(id: int):
    """Pega um usuário com base no ID"""
    resp = read(id, "user")
    return resp


@router.post("/user")
async def create_user(user: User):
    """Cria um usuário"""
    resp = create(user, "user")
    return resp


@router.delete("/user/{id}")
async def delete_user(id: int):
    """Delete um usuário com base no ID"""
    resp = delete(id, "user")
    return resp


@router.put("/user")
async def update_user(user: User):
    """Update um usuário com base no ID"""
    update(user, "user")
    return "Ok"
