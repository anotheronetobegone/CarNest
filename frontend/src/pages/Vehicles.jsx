import VehicleTable from "../components/Vehicles/VehicleTable";
import useVehicles from "../hooks/useVehicles";
import { useState } from "react";
import AddVehicleModal from "../components/Vehicles/AddVehicleModal";
import { createVehicle } from "../services/api";


function Vehicles() {
    const {
        vehicles,
        loading,
        reload
    } = useVehicles();

    const [showModal, setShowModal] = useState(false);

    async function handleSave(vehicle) {
        try {
            await createVehicle(vehicle);
            reload();
            setShowModal(false);
        } catch (error) {
            console.error(error);
        }
    }

    if (loading)
        return <h2>Loading...</h2>;

    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold">
                    Vehicles
                </h1>
                <button
                    onClick={() => setShowModal(true)}
                    className="bg-blue-600 text-white px-4 py-2 rounded"
                >
                    + Add Vehicle
                </button>
            </div>
            <VehicleTable
                vehicles={vehicles}
            />
            {showModal && (
                <AddVehicleModal
                    onClose={() => setShowModal(false)}
                    onSave={handleSave}
                />
            )}
        </div>
    );
}

export default Vehicles;