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


@app.post("/reports", response_model=Report)
async def create_report(report: Report, db: AsyncIOMotorClient = Depends(get_db)):
    report_data = report.model_dump()
    await db.reports.insert_one(report_data)
    logger.info(f"Created report: {report_data}")
    return report_data


@app.get("/reports", response_model=List[Report])
async def read_reports(db: AsyncIOMotorClient = Depends(get_db)):
    reports = db.reports.find()
    reports_list = await reports.to_list(length=None)
    logger.info(f"{reports_list}")
    return reports_list


@app.get("/reports/{username}", response_model=Report)
async def read_report(username: str, db: AsyncIOMotorClient = Depends(get_db)):
    report = await db.reports.find_one({"username": username})
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report


@app.put("/reports/{username}", response_model=Report)
async def update_report(username: str, report: Report, db: AsyncIOMotorClient = Depends(get_db)):
    report_data = report.model_dump()
    result = await db.reports.update_one({"username": str}, {"$set": report_data})

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Report not found")

    report_data["username"] = username
    logger.info(f"Updated report: {report_data}")
    return report_data


@app.delete("/reports/{username}", response_model=Report)
async def delete_report(username: str, db: AsyncIOMotorClient = Depends(get_db)):
    report = await db.reports.find_one_and_delete({"username": username})
    logger.info(f"Deleted report: {report}")

    if report is not None:
        logger.error(f"Failed to delete: {report}")

    return report
