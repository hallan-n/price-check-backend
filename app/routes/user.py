from app.auth.auth import create_access_token, decode_token
from fastapi import HTTPException, Depends



from fastapi import APIRouter, HTTPException
from datetime import timedelta
from app.models.user import User, SimpleUser
from app.database.persistence import create, delete, read, update, read_all, verify_user

router = APIRouter()


@router.get("/user/{id}")
async def get_user(id: int):
    """Pega um usuário com base no ID"""
    resp = read(id, "user")
    return resp


@router.get("/user")
async def get_all_user():
    """Pega todos os usuários"""
    resp = read_all("user")
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
async def update_user(user: User, token: dict = Depends(decode_token)):
    """Update um usuário com base no ID"""
    resp = update(user, "user")
    return resp


@router.post("/token")
async def get_auth(user: SimpleUser):
    """Pega o JWT com base no login"""
    user_auth = verify_user(user)
    print(user_auth)
    if not user_auth:
        raise HTTPException(
            status_code=401,
            detail="Invalid user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user_auth.email})
    return {"access_token": access_token, "token_type": "bearer"}
