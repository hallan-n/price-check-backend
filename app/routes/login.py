from app.services.auth import decode_token
from fastapi import Depends
from fastapi import APIRouter
from app.models.login import Login, LoginSQL
from app.database.persistence import create, read_user_for_email, read_login_for_id

router = APIRouter()
tuple_login = (LoginSQL, LoginSQL.login_id)


@router.post("/login")
async def create_login(login: Login, token: dict = Depends(decode_token)):
    """Cria um login"""
    user = read_user_for_email(token["sub"])
    login_exist = read_login_for_id(store_id=login.store_id, user_id=user.user_id)
    if login_exist:
        print("Login cadastrado")
        return {"resp": "Login já cadastrado"}
    resp = create(login, data_tuple=tuple_login)
    if resp:
        print("Ok")
        return {"resp": "Login criado"}
