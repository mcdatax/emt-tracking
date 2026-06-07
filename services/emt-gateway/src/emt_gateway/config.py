from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "EMT Gateway"
    app_version: str = "0.1.0"
    debug: bool = False

    # EMT Madrid API
    emt_base_url: str = "https://openapi.emtmadrid.es"
    emt_email: str = ""
    emt_password: str = ""

    class Config:
        env_file = ".env"

settings = Settings()