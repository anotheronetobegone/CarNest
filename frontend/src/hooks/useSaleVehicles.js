import { useEffect, useState } from "react";
import { getSaleVehicles } from "../services/api";

export default function useSaleVehicles() {
    const [vehicles, setVehicles] = useState([]);

    useEffect(() => {
        async function loadVehicles() {
            try {
                const response = await getSaleVehicles();
                setVehicles(response.data.vehicles ?? []);
            }
            catch (error) {
                console.log(error);
            }
        }
        loadVehicles();
    }, []);

    return vehicles;
}