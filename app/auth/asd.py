from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"  # Use sua URL de banco de dados

# Configurando o SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definindo o modelo do usuário
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# Criando as tabelas
Base.metadata.create_all(bind=engine)

# Configuração do JWT
SECRET_KEY = "your-secret-key"  # Troque por uma chave secreta mais segura na produção
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Método para criar um usuário e armazenar a senha criptografada
def create_user(db: Session, user: User):
    db_user = User(username=user.username, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Método para obter um usuário pelo nome de usuário
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Método para obter a hash da senha
def get_password_hash(password: str):
    return pwd_context.hash(password)

# Método para verificar a senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Método para gerar JWT sem tempo de expiração
def create_access_token(data: dict):
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependência para obter o esquema JWT

# Rota para registrar um novo usuário
@app.post("/register")
async def register_user(user: User):
    db = SessionLocal()
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user.hashed_password = get_password_hash(user.hashed_password)
    return create_user(db, user)

# Rota para obter token JWT
@app.post("/token", response_model=Token)
async def login_for_access_token(user: User):
    db = SessionLocal()
    db_user = get_user_by_username(db, user.username)
    if not db_user or not verify_password(user.hashed_password, db_user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Gerar token JWT sem tempo de expiração
    access_token = create_access_token(data={"sub": db_user.username})
    
    return {"access_token": access_token, "token_type": "bearer"}

# Rota protegida que requer token JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        db = SessionLocal()
        db_user = get_user_by_username(db, username)
        if db_user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"message": "You are in a protected route!"}
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
