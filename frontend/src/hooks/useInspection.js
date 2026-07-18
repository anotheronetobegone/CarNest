import { useEffect, useState } from "react";
import { getInspections } from "../services/api";

export default function useInspection() {
    const [inspections, setInspections] = useState([]);
    const [loading, setLoading] = useState(true);

    async function loadInspections() {
        try {
            const response = await getInspections();
            setInspections(response.data.inspections ?? []);
        } catch (error) {
            console.error(error);
            setInspections([]);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        loadInspections();
    }, []);

    return {
        inspections,
        loading,
        reload: loadInspections
    };
}