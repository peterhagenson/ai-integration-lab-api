from fastapi import APIRouter, Depends
from db.db_config import get_connection

router = APIRouter()

@router.get("/posts/")
async def get_posts(conn=Depends(get_connection)):
    return await conn.fetch("SELECT * FROM posts")
