from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.database.persistence import create, delete

router = APIRouter()


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
