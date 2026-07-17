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