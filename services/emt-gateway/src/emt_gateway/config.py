from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "EMT Gateway"
    app_version: str = "0.1.0"
    debug: bool = False
    kafka_bootstrap_servers: str = "localhost:9092"

    # EMT Madrid API
    emt_base_url: str = "https://openapi.emtmadrid.es"
    emt_email: str = ""
    emt_password: str = ""
    
    # Polling
    polling_interval_seconds: int = 30
    stops_to_monitor: list[str] = [
        "314",
        "696",
        "1464",
        "722",
        "818",
    ]

    class Config:
        env_file = ".env"

settings = Settings()