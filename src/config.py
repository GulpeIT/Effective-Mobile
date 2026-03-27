from pydantic import Field
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class RunConfig(BaseModel):
    host: str
    port: int

class DataBaseConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    name: str
    
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int
    
    naming_convention: dict = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }

class V1Prefix(BaseModel):
    prefix: str
    auth: str
    user: str
    admin: str

class ApiPrefix(BaseModel):
    prefix: str
    v1: V1Prefix

class AuthUser(BaseModel):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    bearer_path: str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env.template', '.env'),
        env_nested_delimiter='__',
        env_prefix='CONFIG__'
        )
    
    # Настройка запуска приложения
    run: RunConfig
    
    # Настройки базы данных
    db: DataBaseConfig
    
    # Управление префиксами
    api: ApiPrefix
    
    # Авторизация пользователей
    auth : AuthUser
    
    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.db.user}:{self.db.password}@{self.db.host}:{self.db.port}/{self.db.name}"
    
    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.db.user}:{self.db.password}@{self.db.host}:{self.db.port}/{self.db.name}"

settings = Settings()