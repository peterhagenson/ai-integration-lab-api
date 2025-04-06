from fastapi import APIRouter

router = APIRouter()

@router.get("/posts/")
async def get_posts():
    print('in get posts')
