from app.auth.auth import create_access_token
from fastapi import HTTPException
from fastapi import APIRouter, HTTPException
from app.models.user import SimpleUser
from app.database.persistence import verify_user

router = APIRouter()


@router.post("/auth")
async def get_auth(user: SimpleUser):
    """Pega o JWT com base no login"""
    user_auth = verify_user(user)
    if not user_auth:
        raise HTTPException(
            status_code=401,
            detail="Invalid user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data = {"sub": user_auth.email}
    access_token = create_access_token(data=data)
    return {"access_token": access_token, "token_type": "bearer"}
