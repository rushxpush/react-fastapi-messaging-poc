from fastapi import APIRouter
from services.api_gateway.src.version import VERSION

router = APIRouter()

@router.get("/health")
def health():
  # return {"status": "ok", "version": VERSION}
  return {"status": "ok"}

@router.get("/ready")
def ready():
  return {"ready": True}