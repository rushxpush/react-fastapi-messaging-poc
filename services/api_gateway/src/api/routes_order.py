from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

ORDER_SERVICE_URL = 'http://localhost:8001'
headers = {
  'X-Authorization': 'orders-123',
  'Content-Type': 'application/json'
}

@router.post("/orders")
async def create_order(payload: dict):
  """
  API Gateway -> Calls Order microservice via REST
  
  :param payload: Description
  :type payload: dict
  """
  async with httpx.AsyncClient() as client:
    try:
      response = await client.post(f"{ORDER_SERVICE_URL}/orders", json=payload, headers=headers)
      response.raise_for_status()
    except httpx.HTTPError as e:
      raise HTTPException(status_code=500, detail=str(e))
  
  return response.json()
