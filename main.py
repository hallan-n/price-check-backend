from fastapi import FastAPI
from app.routes.user import router as router_user
from app.routes.auth import router as router_auth
from app.routes.product import router as router_product
from app.routes.store import router as router_store
from app.routes.login import router as router_login

app = FastAPI()
app.include_router(router_user)
app.include_router(router_auth)
app.include_router(router_product)
app.include_router(router_store)
app.include_router(router_login)


from app.database.persistence import create_tables; create_tables()
# from app.spiders.data_stores import run_spider; run_spider()
