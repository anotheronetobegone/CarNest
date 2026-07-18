import useInspection from "../hooks/useInspection";

function Inspection() {
    const { inspections, loading } = useInspection();

    if (loading)
        return <h2>Loading...</h2>;

    return (
        <div>
            <h1 className="text-3xl font-bold mb-6">
                Inspection
            </h1>
            <p>Total Inspections: {inspections.length}</p>
        </div>
    );
}

export default Inspection;