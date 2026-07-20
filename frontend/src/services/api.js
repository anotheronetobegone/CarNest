import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const getDashboard = () => 
    api.get("/analytics/dashboard");

export const getVehicles = () =>
    api.get("/vehicles");

export const createVehicle = (vehicle) =>
    api.post("/vehicles", vehicle);

export const updateVehicle = (id, vehicle) =>
    api.put(`/vehicles/${id}`, vehicle);

export const deleteVehicle = (id) =>
    api.delete(`/vehicles/${id}`);

export const getInspections = () =>
    api.get("/inspections");

export const createInspection = (inspection) =>
    api.post("/inspections", inspection);

export const updateInspection = (id, inspection) =>
    api.put(`/inspections/${id}`, inspection);

export const deleteInspection = (id) =>
    api.delete(`/inspections/${id}`);

export const getSales = () =>
    api.get("/sales");

export const getSaleById = (id) =>
    api.get(`/sales/${id}`);

export const createSale = (sale) =>
    api.post("/sales", sale);

export const updateSale = (id, sale) =>
    api.put(`/sales/${id}`, sale);

export const deleteSale = (id) =>
    api.delete(`/sales/${id}`);

export const getSaleVehicles = () =>
    api.get("/sale-vehicles");

export const getAnalyticsDashboard = () =>
    api.get("/analytics/dashboard");

export const getBrandSales = () =>
    api.get("/analytics/brand-sales");

export const getInventorySummary = () =>
    api.get("/analytics/inventory");

export const getInspectionSummary = () =>
    api.get("/analytics/inspection-summary");

export const getMonthlySales = () =>
    api.get("/analytics/monthly-sales");

export default api;