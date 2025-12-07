from fastapi import Header, HTTPException

x_authorization_token = 'orders-123'

def verify_internal(token: str = Header(None, alias="X-Authorization")):
  if token != x_authorization_token:
    raise HTTPException(status_code=401, detail="Unauthorized token")
