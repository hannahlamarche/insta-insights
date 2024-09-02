from fastapi import FastAPI
from .routes import insta_routes

app = FastAPI()

app.include_router(insta_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Insta Analyzer API"}
