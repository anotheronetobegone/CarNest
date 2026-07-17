from fastapi import FastAPI
from db import create_tables

app = FastAPI(
    title="CarNest API",
    description="Used Car Inventory Management & Sales Analytics API",
    version="1.0.0"
)

create_tables()

@app.get("/")
def home():
    """
    Initial endpoint
    """

    return {
        "message": "Welcome to CarNest API",
        "status": "running"
    }