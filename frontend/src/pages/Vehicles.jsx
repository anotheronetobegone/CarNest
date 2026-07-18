import VehicleTable from "../components/Vehicles/VehicleTable";
import useVehicles from "../hooks/useVehicles";
import { useState } from "react";
import AddVehicleModal from "../components/Vehicles/AddVehicleModal";
import { createVehicle, deleteVehicle, updateVehicle } from "../services/api";
import EditVehicleModal from "../components/Vehicles/EditVehicleModal";
import DeleteConfirmModal from "../components/Vehicles/DeleteConfirmModal";


function Vehicles() {
    const {
        vehicles,
        loading,
        reload
    } = useVehicles();

    const [showModal, setShowModal] = useState(false);
    const [editingVehicle, setEditingVehicle] = useState(null);
    const [deletingVehicle, setDeletingVehicle] = useState(null);

    async function handleSave(vehicle) {
        try {
            await createVehicle(vehicle);
            reload();
            setShowModal(false);
        } catch (error) {
            console.error(error);
        }
    }

    async function handleUpdate(vehicleData) {
        try {
            await updateVehicle(
                editingVehicle.vehicle_id,
                vehicleData
            );
            reload();
            setEditingVehicle(null);
        } catch (error) {
            console.error(error);
        }
    }

    async function handleDelete() {
        try {
            await deleteVehicle(deletingVehicle.vehicle_id);
            reload();
            setDeletingVehicle(null);
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
                onEdit={setEditingVehicle}
                onDelete={setDeletingVehicle}
            />
            {showModal && (
                <AddVehicleModal
                    onClose={() => setShowModal(false)}
                    onSave={handleSave}
                />
            )}
            {
            editingVehicle && (
                <EditVehicleModal
                    vehicle={editingVehicle}
                    onClose={() => setEditingVehicle(null)}
                    onSave={handleUpdate}
                />
            )
            }
            {
            deletingVehicle && (
                <DeleteConfirmModal
                    title="Delete Vehicle"
                    message={`Are you sure you want to delete ${deletingVehicle.brand} ${deletingVehicle.model}?`}
                    onCancel={() => setDeletingVehicle(null)}
                    onConfirm={handleDelete}
                />
            )
            }
        </div>
    );
}

export default Vehicles;