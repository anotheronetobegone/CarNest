import { useEffect, useState } from "react";
import { getDashboard } from "../services/api";

export default function useDashboardApi() {
    const [dashboard, setDashboard] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadDashboard() {
            try {

                const response = await getDashboard();
                setDashboard(response.data);
            } catch (error) {
                console.log(error);
            } finally {
                setLoading(false);
            }
        }
        loadDashboard();
    }, []);

    return {
        dashboard,
        loading
    };
}