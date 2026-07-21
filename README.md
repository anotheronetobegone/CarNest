# CarNest - Used Car Inventory & Sales Analytics System

CarNest is a full-stack web application developed to manage the complete lifecycle of a used car dealership. It enables vehicle inventory management, inspection tracking, sales management, and business analytics through an intuitive dashboard.

The project is built using **React**, **FastAPI**, **MySQL**, and **Pandas**, providing both operational management and analytical insights for dealership owners.

---

# Features

## Vehicle Management
- Add new vehicles
- View all vehicles
- Update vehicle details
- Delete vehicles
- Track vehicle status (Available / Sold)

---

## Inspection Management
- Record vehicle inspections
- Update inspection reports
- Delete inspections
- Track inspection status and remarks

---

## Sales Management
- Record vehicle sales
- Calculate profit automatically
- Update sales records
- Delete sales records
- Prevent duplicate sales for the same vehicle

---

## Analytics Dashboard

Business insights generated using **Pandas**:

- Total Vehicles
- Available Vehicles
- Sold Vehicles
- Total Sales
- Total Revenue
- Total Profit
- Brand-wise Sales Analysis
- Monthly Revenue Analysis
- Inventory Summary
- Inspection Status Summary

---

# Tech Stack

## Frontend
- React.js
- React Router
- Axios
- Tailwind CSS

## Backend
- FastAPI
- Python

## Database
- MySQL
- SQLite (Development Support)

## Data Analytics
- Pandas

---

# Project Structure

```
CarNest/
├── main.py
├── db.py
├── analytics.py
├── requirements.txt
├── .env.development
├── test_connection.py
├── frontend/
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── hooks/
│       ├── services/
│       └── App.js
└── tests/
    └── test_vehicle.py
```

---

# Database Design

The project consists of three main tables:

### Vehicles
Stores complete vehicle inventory.

### Inspections
Stores inspection reports linked to vehicles.

### Sales
Stores completed sales and automatically calculates profit.

Relationships:

```
Vehicle
   │
   ├────────► Inspection
   │
   └────────► Sale
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/CarNest.git

cd CarNest
```

---

# Backend Setup

Create a virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
python -m uvicorn main:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Go to frontend

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run React

```bash
npm start
```

Frontend

```
http://localhost:3000
```

---

# API Endpoints

## Vehicles

| Method | Endpoint |
|---------|----------|
| GET | /vehicles |
| GET | /vehicles/{id} |
| POST | /vehicles |
| PUT | /vehicles/{id} |
| DELETE | /vehicles/{id} |

---

## Inspections

| Method | Endpoint |
|---------|----------|
| GET | /inspections |
| GET | /inspections/{id} |
| POST | /inspections |
| PUT | /inspections/{id} |
| DELETE | /inspections/{id} |

---

## Sales

| Method | Endpoint |
|---------|----------|
| GET | /sales |
| GET | /sales/{id} |
| POST | /sales |
| PUT | /sales/{id} |
| DELETE | /sales/{id} |

---

## Analytics

| Method | Endpoint |
|---------|----------|
| GET | /analytics/dashboard |
| GET | /analytics/brand-sales |
| GET | /analytics/inventory |
| GET | /analytics/inspection-summary |
| GET | /analytics/monthly-sales |

---

# Testing

The project includes automated API tests for vehicle CRUD operations using `pytest` and FastAPI's `TestClient`.

## Run the tests

```bash
pip install -r requirements.txt pytest
pytest tests/test_vehicle.py -v
```

The test suite in [tests/test_vehicle.py](tests/test_vehicle.py) covers:
- creating a vehicle
- fetching all vehicles
- fetching a single vehicle by ID
- updating an existing vehicle
- deleting a vehicle

---

# Screenshots

## Dashboard
<img width="1920" height="957" alt="image" src="https://github.com/user-attachments/assets/a9e37f06-6a15-4ac5-a069-8777bc6f5b07" />


---

## Vehicles
<img width="1920" height="957" alt="image" src="https://github.com/user-attachments/assets/a6d51bd4-fc6f-45b5-a659-1c6ee784768a" />

---

## Inspections
<img width="1920" height="957" alt="image" src="https://github.com/user-attachments/assets/a19db037-f9b3-4cab-826f-621ffa1284c2" />

---

## Sales
<img width="1920" height="957" alt="image" src="https://github.com/user-attachments/assets/79bc3ae2-b0da-4b24-8ecd-ab4ff6a93fac" />

---

## Analytics
<img width="1920" height="957" alt="image" src="https://github.com/user-attachments/assets/22a24abc-291a-4420-a616-4cb5da3c4f78" />

---

# Validation

- Duplicate sales are prevented.
- Profit is calculated automatically.
- Vehicle status updates automatically after a sale.
- Foreign key relationships maintain data consistency.

---

# Future Enhancements

- User Authentication
- Role-Based Access Control
- Image Upload for Vehicles
- Search & Filtering
- Pagination
- Export Reports to Excel/PDF
- Interactive Charts (Chart.js/Recharts)
- Cloud Deployment (Azure)

---

# Author

**Parth Ratra**

B.Sc. (Hons.) Computer Science  
Hansraj College, University of Delhi

GitHub: https://github.com/parthratra11

LinkedIn: https://linkedin.com/in/parth-ratra

---

# License

This project is developed for educational and learning purposes.