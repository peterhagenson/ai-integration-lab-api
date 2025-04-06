from fastapi import FastAPI
from api.posts import router as posts_router
from contextlib import asynccontextmanager
from db.db_config import get_db_pool

@asynccontextmanager
async def lifespan(_: FastAPI):
    
    try:
        pool = await get_db_pool()
        async with pool.acquire() as conn:
            version = await conn.fetchval("SELECT version()")
            print(f"Database connection successful: {version}")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise e
    
    yield
    
    global_pool = await get_db_pool()
    if global_pool:
        await global_pool.close()
        print("Database connection pool closed")

app = FastAPI(lifespan=lifespan)

app.include_router(posts_router)