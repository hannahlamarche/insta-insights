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


def str_to_objectid(id_str: str):
    try:
        return ObjectId(id_str)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid ObjectId: {e}")


@app.get("/")
async def read_root(db: AsyncIOMotorClient = Depends(get_db)):
    return {"Hello": "World"}


@app.post("/reports", response_model=Report)
async def create_report(report: Report, db: AsyncIOMotorClient = Depends(get_db)):
    report_data = report.model_dump()
    result = await db.reports.insert_one(report_data)
    report_data["_id"] = str(result.inserted_id)
    logger.info(f"Created report: {report_data}")
    return report_data


@app.get("/reports", response_model=List[Report])
async def read_reports(db: AsyncIOMotorClient = Depends(get_db)):
    reports = db.reports.find()
    reports_list = await reports.to_list(length=None)
    logger.info(f"{reports_list}")
    return reports_list


@app.get("/reports/{report_id}", response_model=Report)
async def read_report(report_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    report = await db.reports.find_one({"_id": str_to_objectid(report_id)})
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report


@app.put("/reports/{report_id}", response_model=Report)
async def update_report(report_id: str, report: Report, db: AsyncIOMotorClient = Depends(get_db)):
    report_data = report.model_dump()
    result = await db.reports.update_one({"_id": str_to_objectid(report_id)}, {"$set": report_data})

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Report not found")

    report_data["_id"] = report_id
    logger.info(f"Updated report: {report_data}")
    return report_data


@app.delete("/reports/{report_id}", response_model=Report)
async def delete_report(report_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    report = await db.reports.find_one_and_delete({"_id": str_to_objectid(report_id)})
    logger.info(f"Deleted report: {report}")

    if report is not None:
        logger.error(f"Report {report_id} was not deleted")

    return report
