from dotenv import load_dotenv

load_dotenv()


import os
from motor.motor_asyncio import AsyncIOMotorClient

_url = f"mongodb://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@localhost:27019"
client = AsyncIOMotorClient(_url)
db = client.rents_db

async def setup_db():
    await db['users'].create_index("login", unique=True)
    await db['users'].create_index("email", unique=True)
