from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  app_env: str = "development"
  redis_url: str = "redis://localhost:6379"
  app_name: str = "mealapp-api-gateway"

settings = Settings()