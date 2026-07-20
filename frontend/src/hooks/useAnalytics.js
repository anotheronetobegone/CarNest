import { useEffect, useState } from "react";
import {
    getAnalyticsDashboard,
    getBrandSales,
    getInventorySummary,
    getInspectionSummary,
    getMonthlySales
} from "../services/api";

export default function useAnalytics() {
    const [dashboard, setDashboard] = useState(null);
    const [brands, setBrands] = useState([]);
    const [inventory, setInventory] = useState({});
    const [inspections, setInspections] = useState({});
    const [monthlySales, setMonthlySales] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadAnalytics() {
            try {
                const [
                    dashboardRes,
                    brandsRes,
                    inventoryRes,
                    inspectionsRes,
                    monthlyRes
                ] = await Promise.all([
                    getAnalyticsDashboard(),
                    getBrandSales(),
                    getInventorySummary(),
                    getInspectionSummary(),
                    getMonthlySales()
                ]);
                setDashboard(dashboardRes.data);
                setBrands(brandsRes.data);
                setInventory(inventoryRes.data);
                setInspections(inspectionsRes.data);
                setMonthlySales(monthlyRes.data);

                console.log(dashboardRes);

                console.log(dashboardRes.data);
            }
            catch (error) {
                console.log(error);
            }
            finally {
                setLoading(false);
            }
        }
        loadAnalytics();
    }, []);

    return {
        dashboard,
        brands,
        inventory,
        inspections,
        monthlySales,
        loading
    };
}