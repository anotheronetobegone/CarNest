from fastapi import FastAPI, HTTPException
from db import create_tables, add_vehicle, get_all_vehicles

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

@app.get("/vehicles")
def get_vehicles():

    try:

        vehicles = get_all_vehicles()

        return {
            "count": len(vehicles),
            "vehicles": vehicles
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
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