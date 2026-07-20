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

│
├── backend/
│   ├── main.py
│   ├── db.py
│   ├── analytics.py
│   ├── requirements.txt
│   └── .env.development
│
├── frontend/
│   ├── src/
│   │
│   ├── components/
│   │
│   ├── pages/
│   │
│   ├── hooks/
│   │
│   ├── services/
│   │
│   └── App.js
│
└── README.md
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

# Screenshots

## Dashboard


---

## Vehicles


---

## Inspections


---

## Sales


---

## Analytics


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