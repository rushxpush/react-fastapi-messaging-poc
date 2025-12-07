from fastapi import FastAPI
from services.orders.src.routes import router as orders_route

app = FastAPI()

app.include_router(orders_route)
