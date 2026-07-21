from fastapi.testclient import TestClient

from main import app
from db import get_connection

client = TestClient(app)

connection = get_connection()
print("Database Connected Successfully!")
connection.close()

def test_create_vehicle():

    response = client.post(
        "/vehicles",
        json={
            "brand": "Honda",
            "model": "City",
            "year": 2023,
            "fuel_type": "Petrol",
            "transmission": "Automatic",
            "color": "White",
            "mileage": 12000,
            "purchase_price": 1000000,
            "selling_price": 1150000,
            "status": "Available"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Vehicle added successfully"

    assert "vehicle_id" in data

def test_get_all_vehicles():

    response = client.get("/vehicles")

    assert response.status_code == 200

    data = response.json()

    assert "vehicles" in data

    assert isinstance(data["vehicles"], list)

def test_get_single_vehicle():

    response = client.get("/vehicles")

    vehicle = response.json()["vehicles"][-1]

    vehicle_id = vehicle["vehicle_id"]

    response = client.get(f"/vehicles/{vehicle_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["vehicle_id"] == vehicle_id

def test_update_vehicle():

    response = client.get("/vehicles")

    vehicle = response.json()["vehicles"][-1]

    vehicle_id = vehicle["vehicle_id"]

    response = client.put(

        f"/vehicles/{vehicle_id}",

        json={
            "brand": "Honda",
            "model": "City ZX",
            "year": 2023,
            "fuel_type": "Petrol",
            "transmission": "Automatic",
            "color": "Black",
            "mileage": 15000,
            "purchase_price": 1000000,
            "selling_price": 1200000,
            "status": "Available"
        }

    )

    assert response.status_code == 200

    assert response.json()["message"] == "Vehicle updated successfully"

def test_delete_vehicle():

    response = client.get("/vehicles")

    vehicle = response.json()["vehicles"][-1]

    vehicle_id = vehicle["vehicle_id"]

    response = client.delete(f"/vehicles/{vehicle_id}")

    assert response.status_code == 200

    assert response.json()["message"] == "Vehicle deleted successfully"