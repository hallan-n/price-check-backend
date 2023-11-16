# from fastapi import FastAPI
# from app.routes.user import router as router_user
# from app.routes.auth import router as router_auth

# # from app.routes.login import router as router_login
# # from app.routes.product import router as router_product
# # from app.routes.store import router as router_store
# app = FastAPI()
# app.include_router(router_user)
# app.include_router(router_auth)
# app.include_router(router_login)
# app.include_router(router_product)
# app.include_router(router_store)

from app.database.persistence import create_tables;create_tables()


# print(a)


from app.spiders.kabum import run_spider_programmatically

run_spider_programmatically()
