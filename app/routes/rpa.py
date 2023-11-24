from app.services.auth import decode_token
from fastapi import Depends
from fastapi import APIRouter
from app.services.rpa_market import run
from app.models.product import Product
from app.models.store import StoreSQL
from app.database.persistence import read_login_for_id, read_user_for_email, read

router = APIRouter()


@router.post("/rpa")
async def run_rpa(product: Product, token: dict = Depends(decode_token)):
    """Pega todas as lojas"""

    user = read_user_for_email(token["sub"])
    store_id = product.store_id
    user_id = user.user_id
    login = read_login_for_id(user_id=user_id, store_id=store_id)
    store = read(data_tuple=(StoreSQL, StoreSQL.store_id), id=product.store_id)
    if login:
        resp = run(product=product, store=store, login=login)
        return resp
    else:
        return {"resp": "Você não possui conta nessa loja"}
