###(запуск приложения и подключение маршрутов)

from fastapi import FastAPI
from fastapi.middleware import Middleware
from app.database import Base, engine
from app.middlewares.log_response_middleware import LogginMiddleware
from app.middlewares.jwt_middleware import JWTMiddleware
from app.routes import auth, get_client_orders, get_master_orders, masters, orders, get_masters  # Подключаем get_masters

middleware = [Middleware(JWTMiddleware)]

app = FastAPI()

app.add_middleware(JWTMiddleware)
app.add_middleware(LogginMiddleware)

Base.metadata.create_all(bind=engine)

# Подключение роутов
app.include_router(auth.router)
app.include_router(masters.router)
app.include_router(orders.router)
app.include_router(get_masters.router)  
app.include_router(get_client_orders.router)
app.include_router(get_master_orders.router)
app.include_router(auth.router)