from pydantic import BaseModel


class Settings(BaseModel):
    project_name: str = "Aurora Digital Assets Backend"
    service_name: str = "aurora-digital-assets-backend"
    version: str = "0.1"
    api_prefix: str = "/api"
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
        "http://localhost:4174",
        "http://127.0.0.1:4174",
    ]


settings = Settings()
