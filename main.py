from fastapi import FastAPI
from app.routes.user import router as router_user
from app.routes.auth import router as router_auth
from app.routes.product import router as router_product
from app.routes.store import router as router_store
from app.routes.login import router as router_login
from app.routes.rpa import router as router_rpa
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8000/auth",
    "http://127.0.0.1:5500",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_user)
app.include_router(router_auth)
app.include_router(router_product)
app.include_router(router_store)
app.include_router(router_login)
app.include_router(router_rpa)


from app.database.persistence import create_tables

create_tables()
# from app.spiders.data_stores import run_spider; run_spider()
