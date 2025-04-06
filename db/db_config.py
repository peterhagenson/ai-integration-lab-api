import asyncpg
from pydantic_settings import BaseSettings

class DatabaseSettings(BaseSettings):
    host: str = 'localhost'
    port: str = '5432'
    user: str
    password: str
    database: str

    class Config:
        env_file = '.env'
        env_prefix = 'POSTGRES_'

db_settings = DatabaseSettings()
db_pool = None

async def get_db_pool():
    global db_pool
    if db_pool is None:
        db_pool = await asyncpg.create_pool(
            host = db_settings.host,
            port = db_settings.port,
            user = db_settings.user,
            password = db_settings.password,
            database = db_settings.database,
            min_size = 5,
            max_size = 20
    )
    return db_pool
