import pandas as pd
from db import get_connection

def load_data():

    conn = get_connection()

    vehicles = pd.read_sql("SELECT * FROM vehicles", conn)
    inspections = pd.read_sql("SELECT * FROM inspections", conn)
    sales = pd.read_sql("SELECT * FROM sales", conn)

    conn.close()

    return vehicles, inspections, sales

def dashboard_summary():

    vehicles, inspections, sales = load_data()

    summary = {

        "total_vehicles": len(vehicles),

        "available_vehicles":
            len(vehicles[vehicles["status"] == "Available"]),

        "sold_vehicles":
            len(vehicles[vehicles["status"] == "Sold"]),

        "total_sales":
            len(sales),

        "total_revenue":
            float(sales["final_price"].sum()) if not sales.empty else 0,

        "total_profit":
            float(sales["profit"].sum()) if not sales.empty else 0
    }

    return summary

def brand_sales():

    vehicles, inspections, sales = load_data()

    if vehicles.empty or sales.empty:
        return []

    merged = sales.merge(
        vehicles,
        on="vehicle_id"
    )

    result = (
        merged
        .groupby("brand")
        .agg(
            vehicles_sold=("sale_id", "count"),
            total_revenue=("final_price", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    return result.to_dict(orient="records")

def inventory_summary():

    vehicles, _, _ = load_data()

    if vehicles.empty:
        return {}

    inventory = (
        vehicles["status"]
        .value_counts()
        .to_dict()
    )

    return inventory

def inspection_summary():

    _, inspections, _ = load_data()

    if inspections.empty:
        return {}

    return (
        inspections["status"]
        .value_counts()
        .to_dict()
    )

def monthly_sales():

    _, _, sales = load_data()

    if sales.empty:
        return []

    sales["sale_date"] = pd.to_datetime(
        sales["sale_date"]
    )

    sales["month"] = sales["sale_date"].dt.strftime("%Y-%m")

    result = (
        sales.groupby("month")
        .agg(
            sales=("sale_id", "count"),
            revenue=("final_price", "sum"),
            profit=("profit", "sum")
        )
        .reset_index()
    )

    return result.to_dict(orient="records")