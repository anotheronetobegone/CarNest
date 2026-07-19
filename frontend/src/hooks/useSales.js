import { useEffect, useState } from "react";
import { getSales } from "../services/api";

export default function useSales() {
    const [sales, setSales] = useState([]);
    const [loading, setLoading] = useState(true);

    async function loadSales() {
        try {
            const response = await getSales();
            setSales(response.data.sales ?? []);
        }
        catch (error) {
            console.log(error);
            setSales([]);
        }
        finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        loadSales();
    }, []);

    return {
        sales,
        loading,
        reload: loadSales
    };
}