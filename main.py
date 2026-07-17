from fastapi import FastAPI, HTTPException
from db import create_tables, add_vehicle

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

@app.post("/vehicles")
def create_vehicle(vehicle: dict):

    try:

        vehicle_id = add_vehicle(vehicle)

        return {
            "message": "Vehicle added successfully",
            "vehicle_id": vehicle_id
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )