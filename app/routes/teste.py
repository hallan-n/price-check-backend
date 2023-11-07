from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def teste():
    """Teste de retorno"""
    return {"msg": "rodando"}
