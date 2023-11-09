from fastapi import FastAPI
from app.routes.user import router as router_user
from app.routes.login import router as router_login
from app.routes.product import router as router_product
from app.routes.store import router as router_store

app = FastAPI()
app.include_router(router_user)
app.include_router(router_login)
app.include_router(router_product)
app.include_router(router_store)
