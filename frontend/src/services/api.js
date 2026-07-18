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

export default api;