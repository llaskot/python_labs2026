
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.database import client, setup_db
from app.users import users_router
from app.auth import auth_router



@asynccontextmanager
async def lifespan(_: FastAPI):
    await setup_db()
    print("🚀 Database is ready")
    yield
    client.close()

app = FastAPI(lifespan=lifespan)
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.get("/hello")
async def read_hello():
    return FileResponse("static/hello.html")


app.include_router(users_router)
app.include_router(auth_router)





