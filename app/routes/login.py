from app.services.auth import decode_token
from fastapi import Depends
from fastapi import APIRouter
from app.models.login import Login, LoginSQL
from app.database.persistence import create, read_user_for_email

router = APIRouter()
tuple_login = (LoginSQL, LoginSQL.login_id)

@router.post("/login")
async def create_product(login: Login, token: dict = Depends(decode_token)):
    """Cria um login"""
    user = read_user_for_email(token["sub"])
    login.user_id = user.user_id
    resp = create(login, data_tuple=tuple_login)
    return resp
