
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import client, setup_db
from app.users import users_router
from app.auth import auth_router
from app.ips import ips_router
from front import pages_router
from app.books import book_router



@asynccontextmanager
async def lifespan(_: FastAPI):
    await setup_db()
    print("🚀 Database is ready")
    yield
    client.close()

app = FastAPI(lifespan=lifespan)


app.include_router(users_router)
app.include_router(auth_router)
app.include_router(ips_router)
app.include_router(pages_router)

app.include_router(book_router)





