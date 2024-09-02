from motor.motor_asyncio import AsyncIOMotorClient
from typing import Annotated
from fastapi import Depends
from pydantic import BeforeValidator
from config import settings


client = AsyncIOMotorClient(settings.mongodb_uri)


def get_db(testing: bool = False) -> AsyncIOMotorClient:
    db_name = settings.test_mongodb_database if testing else settings.mongodb_database
    db = client[db_name]
    try:
        yield db
    finally:
        pass


MongoDBDeps = Annotated[AsyncIOMotorClient, Depends(lambda: get_db(testing=False))]
PyObjectId = Annotated[str, BeforeValidator(str)]
