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