from app.services.auth import decode_token
from fastapi import Depends
from fastapi import APIRouter
from app.services.rpa_market import run
from app.models.product import Product
router = APIRouter()


@router.post("/rpa")
async def run_rpa(product: Product, token: dict = Depends(decode_token)):
    """Pega todas as lojas"""
    print(product)
    # run()
    # return "ok"



