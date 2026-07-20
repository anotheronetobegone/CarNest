"""FastAPI application for the CarNest inventory and sales management API."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from analytics import (
    brand_sales,
    dashboard_summary,
    inspection_summary,
    inventory_summary,
    monthly_sales,
)
from db import (
    add_inspection,
    add_sale,
    add_vehicle,
    create_tables,
    delete_inspection,
    delete_sale,
    delete_vehicle,
    get_all_inspections,
    get_all_sales,
    get_all_vehicles,
    get_inspection_by_id,
    get_sale_by_id,
    get_sale_eligible_vehicles,
    get_vehicle_by_id,
    update_inspection,
    update_sale,
    update_vehicle,
)

app = FastAPI(
    title="CarNest API",
    description="Used Car Inventory Management & Sales Analytics API",
    version="1.0.0",
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
    """Return the API welcome message."""

    return {"message": "Welcome to CarNest API", "status": "running"}


@app.get("/vehicles")
def get_vehicles():
    """Retrieve all vehicles."""

    try:
        vehicles = get_all_vehicles()
        return {"count": len(vehicles), "vehicles": vehicles}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/vehicles/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    """Retrieve one vehicle by its ID."""

    vehicle = get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return vehicle


@app.post("/vehicles")
def create_vehicle(vehicle: dict):
    """Create a new vehicle entry."""

    try:
        vehicle_id = add_vehicle(vehicle)
        return {"message": "Vehicle added successfully", "vehicle_id": vehicle_id}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.put("/vehicles/{vehicle_id}")
def edit_vehicle(vehicle_id: int, vehicle: dict):
    """Update an existing vehicle."""

    updated = update_vehicle(vehicle_id, vehicle)

    if updated == 0:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return {"message": "Vehicle updated successfully"}


@app.delete("/vehicles/{vehicle_id}")
def remove_vehicle(vehicle_id: int):
    """Delete a vehicle by its ID."""

    deleted = delete_vehicle(vehicle_id)

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return {"message": "Vehicle deleted successfully"}


@app.post("/inspections")
def create_inspection(inspection: dict):
    """Create a new inspection record."""

    try:
        inspection_id = add_inspection(inspection)
        return {
            "message": "Inspection added successfully",
            "inspection_id": inspection_id,
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/inspections")
def get_inspections():
    """Retrieve all inspections."""

    inspections = get_all_inspections()

    return {"count": len(inspections), "inspections": inspections}


@app.get("/inspections/{inspection_id}")
def get_inspection(inspection_id: int):
    """Retrieve one inspection by its ID."""

    inspection = get_inspection_by_id(inspection_id)

    if inspection is None:
        raise HTTPException(status_code=404, detail="Inspection not found")

    return inspection


@app.put("/inspections/{inspection_id}")
def edit_inspection(inspection_id: int, inspection: dict):
    """Update an existing inspection."""

    updated = update_inspection(inspection_id, inspection)

    if updated == 0:
        raise HTTPException(status_code=404, detail="Inspection not found")

    return {"message": "Inspection updated successfully"}


@app.delete("/inspections/{inspection_id}")
def remove_inspection(inspection_id: int):
    """Delete an inspection by its ID."""

    deleted = delete_inspection(inspection_id)

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Inspection not found")

    return {"message": "Inspection deleted successfully"}


@app.post("/sales")
def create_sale(sale: dict):
    """Record a new vehicle sale."""

    result = add_sale(sale)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])

    return {
        "message": "Sale recorded successfully.",
        "sale_id": result["sale_id"],
        "profit": result["profit"],
    }


@app.get("/sales")
def get_sales():
    """Retrieve all sales."""

    sales = get_all_sales()

    return {"count": len(sales), "sales": sales}


@app.get("/sales/{sale_id}")
def get_sale(sale_id: int):
    """Retrieve one sale by its ID."""

    sale = get_sale_by_id(sale_id)

    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")

    return sale


@app.put("/sales/{sale_id}")
def edit_sale(sale_id: int, sale: dict):
    """Update an existing sale."""

    updated = update_sale(sale_id, sale)

    if updated == 0:
        raise HTTPException(status_code=404, detail="Sale not found")

    return {"message": "Sale updated successfully"}


@app.delete("/sales/{sale_id}")
def remove_sale(sale_id: int):
    """Delete a sale by its ID."""

    deleted = delete_sale(sale_id)

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Sale not found")

    return {"message": "Sale deleted successfully"}


@app.get("/sale-vehicles")
def get_sale_vehicles():
    """Return vehicles eligible for a sale."""

    vehicles = get_sale_eligible_vehicles()

    return {"count": len(vehicles), "vehicles": vehicles}


@app.get("/analytics/dashboard")
def analytics_dashboard():
    """Return the dashboard summary metrics."""

    return dashboard_summary()


@app.get("/analytics/brand-sales")
def analytics_brand_sales():
    """Return brand-level sales analytics."""

    return brand_sales()


@app.get("/analytics/inventory")
def analytics_inventory():
    """Return vehicle inventory analytics."""

    return inventory_summary()


@app.get("/analytics/inspection-summary")
def analytics_inspections():
    """Return inspection status analytics."""

    return inspection_summary()


@app.get("/analytics/monthly-sales")
def analytics_monthly_sales():
    """Return monthly sales analytics."""

    return monthly_sales()
