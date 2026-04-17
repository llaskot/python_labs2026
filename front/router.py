import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(
    tags=["Frontend"]
)

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
STATIC_DIR = os.path.join(CURRENT_DIR, "static")

@router.get("/")
async def read_index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@router.get("/hello")
async def read_hello():
    return FileResponse(os.path.join(STATIC_DIR, "hello.html"))
