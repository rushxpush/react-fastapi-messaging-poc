from fastapi import FastAPI
from services.api_gateway.src.api.routes_health import router as health_router
from services.api_gateway.src.api.routes_order import router as order_router
from pydantic import BaseModel

app = FastAPI()

app.include_router(health_router)
app.include_router(order_router)

