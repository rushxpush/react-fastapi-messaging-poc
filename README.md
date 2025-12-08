# React FastAPI Messaging POC

```bash
# Docker

```

```bash
# Enter Poetry shell
poetry shell

# Development
poetry run uvicorn services.api_gateway.src.main:app --reload
poetry run uvicorn services.orders.src.main:app --reload

# Production
poetry run gunicorn services.api_gateway.src.main:app \
  -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```
