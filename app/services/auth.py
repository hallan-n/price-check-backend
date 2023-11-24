from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException, Header
from jose import JWTError, jwt
from dotenv import load_dotenv
from os import getenv

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def data_hash(data: str):
    return pwd_context.hash(data)


def verify_hash(data, data_hash):
    return pwd_context.verify(data, data_hash)


SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {**data, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str = Header(...)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token incorreto ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
