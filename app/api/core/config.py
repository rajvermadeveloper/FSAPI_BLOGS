from pydantic_settings import BaseSettings

class MySQLSettings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DATABASE: str

    class Config:
        env_file = ".env"
        case_sensitive = True
    
    
mysql_settings = MySQLSettings()