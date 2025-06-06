from fastapi import FastAPI
from app.database import Base, engine
from app.routes import master, client, order  # подключим потом нужные модули
from app.middlewares.jwt_middleware import JWTMiddleware
from app.middlewares.log_response_middleware import LogginMiddleware

app = FastAPI(
    title="ServiceApp",
    description="Backend for managing masters, clients, and orders",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(JWTMiddleware)
app.add_middleware(LogginMiddleware)

app.include_router(master.router, prefix="/masters", tags=["Masters"])
app.include_router(client.router, prefix="/clients", tags=["Clients"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
