import { useEffect, useState } from "react";
import { getVehicles } from "../services/api";

export default function useVehicles() {

    const [vehicles, setVehicles] = useState([]);
    const [loading, setLoading] = useState(true);

    async function loadVehicles() {
        try {
            const response = await getVehicles();
            setVehicles(response.data.vehicles ?? []);
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        loadVehicles();
    }, []);

    return {
        vehicles,
        loading,
        reload: loadVehicles
    };
}   