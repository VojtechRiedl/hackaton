
from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict

from sqlalchemy.engine.url import URL

class DatabaseConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    name: str

    def to_sqlalchemy_url(self):
        return URL.create(
            drivername="mariadb+pymysql",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name,
        )


class Settings(BaseSettings):
    database: DatabaseConfig

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        arbitrary_types_allowed=True,
        env_nested_delimiter="__",
    )

settings = Settings()