from app.auth.auth import decode_token
from fastapi import Depends
from fastapi import APIRouter
from app.models.user import User, UserSQL
from app.database.persistence import (
    create,
    read_user_for_email,
    update
)

router = APIRouter()

tuple_user = (UserSQL, UserSQL.user_id, UserSQL.email)


@router.get("/user")
async def get_user(token: dict = Depends(decode_token)):
    """Pega os dados do usuário autenticado"""
    resp = read_user_for_email(token["sub"])
    return resp


@router.post("/user")
async def create_user(user: User):
    """Cria um usuário"""
    resp = create(user, tuple_user)
    return resp


@router.put("/user")
async def update_user(user: User, token: dict = Depends(decode_token)):
    """Atualiza um usuário"""
    resp = update(value=user, data_tuple=tuple_user, token=token["sub"])
    return resp
