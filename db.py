import os
import sqlite3
import mysql.connector
from dotenv import load_dotenv

load_dotenv(".env.development")

DB_TYPE = os.getenv("DB_TYPE")


def get_placeholder():
    """
    Returns the SQL placeholder based on the database type.
    """
    return "?" if DB_TYPE == "sqlite" else "%s"


def get_connection():
    """
    Returns a connection based on the database type.
    """

    if DB_TYPE == "sqlite":
        return sqlite3.connect(os.getenv("DB_PATH"))

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def create_tables():
    """
    Creates all required tables if they don't already exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    if DB_TYPE == "sqlite":

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicles (
                vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                fuel_type TEXT NOT NULL,
                transmission TEXT NOT NULL,
                color TEXT NOT NULL,
                mileage INTEGER NOT NULL,
                purchase_price REAL NOT NULL,
                selling_price REAL,
                status TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inspections (
                inspection_id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_id INTEGER NOT NULL,
                inspection_date TEXT,
                condition TEXT,
                remarks TEXT,
                status TEXT,
                FOREIGN KEY(vehicle_id)
                REFERENCES vehicles(vehicle_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_id INTEGER UNIQUE,
                buyer_name TEXT NOT NULL,
                sale_date TEXT,
                final_price REAL,
                profit REAL,
                FOREIGN KEY(vehicle_id)
                REFERENCES vehicles(vehicle_id)
            )
        """)

    else:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicles (
                vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
                brand VARCHAR(50) NOT NULL,
                model VARCHAR(50) NOT NULL,
                year INT NOT NULL,
                fuel_type VARCHAR(30) NOT NULL,
                transmission VARCHAR(30) NOT NULL,
                color VARCHAR(30) NOT NULL,
                mileage INT NOT NULL,
                purchase_price DECIMAL(10,2) NOT NULL,
                selling_price DECIMAL(10,2),
                status VARCHAR(20) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inspections (
                inspection_id INT AUTO_INCREMENT PRIMARY KEY,
                vehicle_id INT NOT NULL,
                inspection_date DATE,
                `condition` VARCHAR(50),
                remarks TEXT,
                status VARCHAR(20),
                FOREIGN KEY(vehicle_id)
                REFERENCES vehicles(vehicle_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INT AUTO_INCREMENT PRIMARY KEY,
                vehicle_id INT UNIQUE,
                buyer_name VARCHAR(100) NOT NULL,
                sale_date DATE,
                final_price DECIMAL(10,2),
                profit DECIMAL(10,2),
                FOREIGN KEY(vehicle_id)
                REFERENCES vehicles(vehicle_id)
            )
        """)

    conn.commit()
    conn.close()


# VEHICLE


def vehicle_exists(vehicle_id):
    """
    Checks if a vehicle exists.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        SELECT COUNT(*)
        FROM vehicles
        WHERE vehicle_id = {placeholder}
    """

    cursor.execute(query, (vehicle_id,))

    count = cursor.fetchone()[0]

    conn.close()

    return count > 0


def get_vehicle_status(vehicle_id):
    """
    Returns the current status of a vehicle.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        SELECT status
        FROM vehicles
        WHERE vehicle_id = {placeholder}
    """

    cursor.execute(query, (vehicle_id,))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return row[0]


def vehicle_to_dict(row):
    return {
        "vehicle_id": row[0],
        "brand": row[1],
        "model": row[2],
        "year": row[3],
        "fuel_type": row[4],
        "transmission": row[5],
        "color": row[6],
        "mileage": row[7],
        "purchase_price": row[8],
        "selling_price": row[9],
        "status": row[10],
    }


def get_all_vehicles():
    """
    Returns all vehicles from the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM vehicles
    """)

    rows = cursor.fetchall()

    conn.close()

    vehicles = [vehicle_to_dict(row) for row in rows]

    return vehicles


def get_vehicle_by_id(vehicle_id):
    """
    Returns a single vehicle by its ID.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM vehicles
        WHERE vehicle_id = ?
    """,
        (vehicle_id,),
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return vehicle_to_dict(row)


def add_vehicle(data):
    """
    Inserts a new vehicle into the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
    INSERT INTO vehicles (
        brand,
        model,
        year,
        fuel_type,
        transmission,
        color,
        mileage,
        purchase_price,
        selling_price,
        status
    )
    VALUES (
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder}
    )
    """

    cursor.execute(
        query,
        (
            data["brand"],
            data["model"],
            data["year"],
            data["fuel_type"],
            data["transmission"],
            data["color"],
            data["mileage"],
            data["purchase_price"],
            data["selling_price"],
            data["status"],
        ),
    )

    conn.commit()

    vehicle_id = cursor.lastrowid

    conn.close()

    return vehicle_id


def update_vehicle(vehicle_id, data):
    """
    Updates an existing vehicle.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE vehicles
        SET
            brand = ?,
            model = ?,
            year = ?,
            fuel_type = ?,
            transmission = ?,
            color = ?,
            mileage = ?,
            purchase_price = ?,
            selling_price = ?,
            status = ?
        WHERE vehicle_id = ?
    """,
        (
            data["brand"],
            data["model"],
            data["year"],
            data["fuel_type"],
            data["transmission"],
            data["color"],
            data["mileage"],
            data["purchase_price"],
            data["selling_price"],
            data["status"],
            vehicle_id,
        ),
    )

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return updated


def delete_vehicle(vehicle_id):
    """
    Deletes a vehicle.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM vehicles
        WHERE vehicle_id = ?
    """,
        (vehicle_id,),
    )

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted


# INSPECTION


def add_inspection(data):
    """
    Adds a vehicle inspection.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
    INSERT INTO inspections(
        vehicle_id,
        inspection_date,
        condition,
        remarks,
        status
    )
    VALUES (
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder},
        {placeholder}
    )
    """

    cursor.execute(
        query,
        (
            data["vehicle_id"],
            data["inspection_date"],
            data["condition"],
            data["remarks"],
            data["status"],
        ),
    )

    conn.commit()

    inspection_id = cursor.lastrowid

    conn.close()

    return inspection_id


def get_all_inspections():
    """
    Returns all inspections.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            i.inspection_id,
            i.vehicle_id,
            CONCAT(v.brand, ' ', v.model) AS vehicle_name,
            i.inspection_date,
            i.condition,
            i.remarks,
            i.status

        FROM inspections i

        JOIN vehicles v
        ON i.vehicle_id = v.vehicle_id
    """)

    rows = cursor.fetchall()

    conn.close()

    inspections = []

    for row in rows:
        inspections.append(
            {
                "inspection_id": row[0],
                "vehicle_id": row[1],
                "vehicle_name": row[2],
                "inspection_date": row[3],
                "condition": row[4],
                "remarks": row[5],
                "status": row[6],
            }
        )

    return inspections


def get_inspection_by_id(inspection_id):
    """
    Returns an inspection by ID.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        SELECT
            i.inspection_id,
            i.vehicle_id,
            CONCAT(v.brand, ' ', v.model) AS vehicle_name,
            i.inspection_date,
            i.condition,
            i.remarks,
            i.status
        FROM inspections i
        JOIN vehicles v
            ON i.vehicle_id = v.vehicle_id
        WHERE i.inspection_id = {placeholder}
    """

    cursor.execute(query, (inspection_id,))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return {
        "inspection_id": row[0],
        "vehicle_id": row[1],
        "vehicle_name": row[2],
        "inspection_date": row[3],
        "condition": row[4],
        "remarks": row[5],
        "status": row[6],
    }


def update_inspection(inspection_id, data):
    """
    Updates an inspection.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        UPDATE inspections
        SET
            vehicle_id={placeholder},
            inspection_date={placeholder},
            condition={placeholder},
            remarks={placeholder},
            status={placeholder}
        WHERE inspection_id={placeholder}
    """

    cursor.execute(
        query,
        (
            data["vehicle_id"],
            data["inspection_date"],
            data["condition"],
            data["remarks"],
            data["status"],
            inspection_id,
        ),
    )

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return updated


def delete_inspection(inspection_id):
    """
    Deletes an inspection.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        DELETE FROM inspections
        WHERE inspection_id={placeholder}
    """

    cursor.execute(query, (inspection_id,))

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted


# HELPER FUNCTIONS


def calculate_profit(vehicle_id, selling_price):
    """
    Calculates the profit made on a vehicle sale.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        SELECT purchase_price
        FROM vehicles
        WHERE vehicle_id = {placeholder}
    """

    cursor.execute(query, (vehicle_id,))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    purchase_price = row[0]

    return selling_price - purchase_price


def mark_vehicle_as_sold(vehicle_id):
    """
    Updates vehicle status to Sold.
    """

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        UPDATE vehicles
        SET status = {placeholder}
        WHERE vehicle_id = {placeholder}
    """

    cursor.execute(query, ("Sold", vehicle_id))

    conn.commit()

    conn.close()


def mark_vehicle_as_available(vehicle_id):

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        UPDATE vehicles
        SET status={placeholder}
        WHERE vehicle_id={placeholder}
    """

    cursor.execute(query, ("Available", vehicle_id))

    conn.commit()
    conn.close()


def get_sale_eligible_vehicles():
    """
    Returns vehicles that can be sold.
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT DISTINCT
            v.vehicle_id,
            v.brand,
            v.model,
            v.purchase_price
        FROM vehicles v
        JOIN inspections i
            ON v.vehicle_id = i.vehicle_id
        WHERE
            v.status='Available'
            AND i.status='Passed'
        ORDER BY
            v.brand,
            v.model
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    vehicles = []

    for row in rows:

        vehicles.append(
            {
                "vehicle_id": row[0],
                "brand": row[1],
                "model": row[2],
                "purchase_price": row[3],
            }
        )

    return vehicles


# SALES


def add_sale(data):
    """
    Creates a new vehicle sale.
    """

    vehicle_id = data["vehicle_id"]

    # Check if vehicle exists
    if not vehicle_exists(vehicle_id):
        return {"success": False, "message": "Vehicle does not exist."}

    # Check vehicle status
    status = get_vehicle_status(vehicle_id)

    if status != "Available":
        return {"success": False, "message": "Vehicle is not available for sale."}

    # Calculate profit
    profit = calculate_profit(vehicle_id, data["final_price"])

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        INSERT INTO sales (
            vehicle_id,
            buyer_name,
            sale_date,
            final_price,
            profit
        )
        VALUES (
            {placeholder},
            {placeholder},
            {placeholder},
            {placeholder},
            {placeholder}
        )
    """

    cursor.execute(
        query,
        (
            vehicle_id,
            data["buyer_name"],
            data["sale_date"],
            data["final_price"],
            profit,
        ),
    )

    conn.commit()

    sale_id = cursor.lastrowid

    conn.close()

    # Update vehicle status
    mark_vehicle_as_sold(vehicle_id)

    return {"success": True, "sale_id": sale_id, "profit": profit}


def get_all_sales():
    """
    Returns all sales.
    """

    conn = get_connection()
    cursor = conn.cursor()
    placeholder = get_placeholder()

    query = f"""
        SELECT
            s.sale_id,
            s.vehicle_id,
            CONCAT(v.brand, ' ', v.model) AS vehicle_name,
            s.buyer_name,
            s.sale_date,
            s.final_price,
            s.profit
        FROM sales s
        JOIN vehicles v
            ON s.vehicle_id = v.vehicle_id
        ORDER BY s.sale_date DESC
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    sales = []

    for row in rows:
        sales.append(
            {
                "sale_id": row[0],
                "vehicle_id": row[1],
                "vehicle_name": row[2],
                "buyer_name": row[3],
                "sale_date": row[4],
                "final_price": row[5],
                "profit": row[6],
            }
        )
    return sales


def get_sale_by_id(sale_id):
    """
    Returns a sale by ID.
    """

    conn = get_connection()
    cursor = conn.cursor()
    placeholder = get_placeholder()

    query = f"""
        SELECT
            s.sale_id,
            s.vehicle_id,
            CONCAT(v.brand, ' ', v.model) AS vehicle_name,
            s.buyer_name,
            s.sale_date,
            s.final_price,
            s.profit
        FROM sales s
        JOIN vehicles v
            ON s.vehicle_id = v.vehicle_id
        WHERE s.sale_id = {placeholder}
    """

    cursor.execute(query, (sale_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "sale_id": row[0],
        "vehicle_id": row[1],
        "vehicle_name": row[2],
        "buyer_name": row[3],
        "sale_date": row[4],
        "final_price": row[5],
        "profit": row[6],
    }


def update_sale(sale_id, data):
    """
    Updates a sale.
    """

    profit = calculate_profit(data["vehicle_id"], data["final_price"])

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        UPDATE sales
        SET
            buyer_name={placeholder},
            sale_date={placeholder},
            final_price={placeholder},
            profit={placeholder}
        WHERE sale_id={placeholder}
    """

    cursor.execute(
        query,
        (data["buyer_name"], data["sale_date"], data["final_price"], profit, sale_id),
    )

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return updated


def delete_sale(sale_id):

    conn = get_connection()
    cursor = conn.cursor()

    placeholder = get_placeholder()

    query = f"""
        SELECT vehicle_id
        FROM sales
        WHERE sale_id={placeholder}
    """

    cursor.execute(query, (sale_id,))
    row = cursor.fetchone()

    if row is None:
        conn.close()
        return 0

    vehicle_id = row[0]

    query = f"""
        DELETE FROM sales
        WHERE sale_id={placeholder}
    """

    cursor.execute(query, (sale_id,))

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    if deleted:
        mark_vehicle_as_available(vehicle_id)

    return deleted
