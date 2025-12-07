from fastapi import APIRouter, Depends
from services.orders.src.service import verify_internal

router = APIRouter()

@router.post("/orders", dependencies=[Depends(verify_internal)])
async def create_order(payload: dict):
  return {"status": "ok"}

@router.get("/health")
def health():
  return {"status": "ok", "service": "orders"}

