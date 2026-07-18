from fastapi import FastAPI, HTTPException
from db import (
    # VEHICLES
    create_tables,
    add_vehicle,
    get_all_vehicles,
    get_vehicle_by_id,
    update_vehicle,
    delete_vehicle,

    # INSPECTION
    add_inspection,
    get_all_inspections,
    get_inspection_by_id,
    update_inspection,
    delete_inspection,

    # SALES
    add_sale,
    get_all_sales,
    get_sale_by_id,
    update_sale,
    delete_sale
)

from analytics import (
    dashboard_summary,
    brand_sales,
    inventory_summary,
    inspection_summary,
    monthly_sales
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CarNest API",
    description="Used Car Inventory Management & Sales Analytics API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

# VEHICLES
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
    
@app.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):

    vehicle = get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return vehicle
    
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
    
@app.put("/vehicles/{vehicle_id}")
def edit_vehicle(vehicle_id: int, vehicle: dict):

    updated = update_vehicle(vehicle_id, vehicle)

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return {
        "message": "Vehicle updated successfully"
    }

@app.delete("/vehicles/{vehicle_id}")
def remove_vehicle(vehicle_id: int):

    deleted = delete_vehicle(vehicle_id)

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return {
        "message": "Vehicle deleted successfully"
    }

# INSPECTION
@app.post("/inspections")
def create_inspection(inspection: dict):

    try:

        inspection_id = add_inspection(inspection)

        return {
            "message": "Inspection added successfully",
            "inspection_id": inspection_id
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@app.get("/inspections")
def get_inspections():

    inspections = get_all_inspections()

    return {
        "count": len(inspections),
        "inspections": inspections
    }

@app.get("/inspections/{inspection_id}")
def get_inspection(inspection_id: int):

    inspection = get_inspection_by_id(inspection_id)

    if inspection is None:
        raise HTTPException(
            status_code=404,
            detail="Inspection not found"
        )

    return inspection

@app.put("/inspections/{inspection_id}")
def edit_inspection(inspection_id: int, inspection: dict):

    updated = update_inspection(inspection_id, inspection)

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Inspection not found"
        )

    return {
        "message": "Inspection updated successfully"
    }

@app.delete("/inspections/{inspection_id}")
def remove_inspection(inspection_id: int):

    deleted = delete_inspection(inspection_id)

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Inspection not found"
        )

    return {
        "message": "Inspection deleted successfully"
    }

# SALES

@app.post("/sales")
def create_sale(sale: dict):

    result = add_sale(sale)

    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail=result["message"]
        )

    return {
        "message": "Sale recorded successfully.",
        "sale_id": result["sale_id"],
        "profit": result["profit"]
    }

@app.get("/sales")
def get_sales():

    sales = get_all_sales()

    return {
        "count": len(sales),
        "sales": sales
    }

@app.get("/sales/{sale_id}")
def get_sale(sale_id: int):

    sale = get_sale_by_id(sale_id)

    if sale is None:
        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    return sale

@app.put("/sales/{sale_id}")
def edit_sale(sale_id: int, sale: dict):

    updated = update_sale(sale_id, sale)

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    return {
        "message": "Sale updated successfully"
    }

@app.delete("/sales/{sale_id}")
def remove_sale(sale_id: int):

    deleted = delete_sale(sale_id)

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    return {
        "message": "Sale deleted successfully"
    }

@app.get("/analytics/dashboard")
def analytics_dashboard():

    return dashboard_summary()

@app.get("/analytics/brand-sales")
def analytics_brand_sales():

    return brand_sales()

@app.get("/analytics/inventory")
def analytics_inventory():

    return inventory_summary()

@app.get("/analytics/inspection-summary")
def analytics_inspections():

    return inspection_summary()

@app.get("/analytics/monthly-sales")
def analytics_monthly_sales():

    return monthly_sales()