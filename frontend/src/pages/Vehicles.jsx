import VehicleTable from "../components/Vehicles/VehicleTable";
import useVehicles from "../hooks/useVehicles";

function Vehicles() {
    const {
        vehicles,
        loading
    } = useVehicles();

    if (loading)
        return <h2>Loading...</h2>;

    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold">
                    Vehicles
                </h1>
                <button className="bg-blue-600 text-white px-4 py-2 rounded">
                    + Add Vehicle
                </button>
            </div>
            <VehicleTable
                vehicles={vehicles}
            />
        </div>
    );
}

export default Vehicles;