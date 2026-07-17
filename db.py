import os
import sqlite3
import mysql.connector
from dotenv import load_dotenv

# Load development environment
load_dotenv(".env.development")

DB_TYPE = os.getenv("DB_TYPE")


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
        database=os.getenv("DB_NAME")
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
        "status": row[10]
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

    cursor.execute("""
        SELECT * FROM vehicles
        WHERE vehicle_id = ?
    """, (vehicle_id,))

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

    cursor.execute("""
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["brand"],
        data["model"],
        data["year"],
        data["fuel_type"],
        data["transmission"],
        data["color"],
        data["mileage"],
        data["purchase_price"],
        data["selling_price"],
        data["status"]
    ))

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

    cursor.execute("""
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
    """, (
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
        vehicle_id
    ))

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return updated