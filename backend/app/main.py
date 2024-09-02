from models.Report import Report
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from deps import get_db
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
import logging

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
async def read_root(db: AsyncIOMotorClient = Depends(get_db)):
    return {"Hello": "World"}


@app.get("/reports", response_model=List[Report])
async def read_reports(db: AsyncIOMotorClient = Depends(get_db)):
    reports = db.reports.find()
    reports_list = await reports.to_list(length=None)
    logger.info(f"{reports_list}")
    return reports_list
