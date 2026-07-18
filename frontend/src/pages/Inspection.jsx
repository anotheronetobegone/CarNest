import { useState } from "react";
import InspectionTable from "../components/Inspection/InspectionTable";
import useInspection from "../hooks/useInspection";
import { createInspection, deleteInspection, updateInspection } from "../services/api";
import EditInspectionModal from "../components/Inspection/EditInspectionModal";
import DeleteConfirmModal from "../components/Vehicles/DeleteConfirmModal";
import useVehicles from "../hooks/useVehicles";
import AddInspectionModal from "../components/Inspection/AddInspectionModal";

function Inspection() {
    const {
        inspections,
        loading,
        reload
    } = useInspection();

    const {
        vehicles,
    } = useVehicles();

    const [showModal, setShowModal] = useState(false);
    const [editingInspection, setEditingInspection] = useState(null);
    const [deletingInspection, setDeletingInspection] = useState(null);

    if (loading)
        return <h2>Loading...</h2>;

    async function handleSave(data) {
        try {
            await createInspection(data);
            reload();
            setShowModal(false);
        }
        catch (error) {
            console.error(error);
        }
    }

    async function handleUpdate(data) {
        try {
            await updateInspection(
                editingInspection.inspection_id,
                data
            );
            reload();
            setEditingInspection(null);
        }
        catch (error) {
            console.error(error);
        }
    }

    async function handleDelete() {
        try {
            await deleteInspection(
                deletingInspection.inspection_id
            );
            reload();
            setDeletingInspection(null);
        }
        catch (error) {
            console.error(error);
        }
    }

    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold">
                    Inspection
                </h1>
                <button 
                className="bg-blue-600 text-white px-4 py-2 rounded"
                onClick={() => setShowModal(true)}>
                    + New Inspection
                </button>
            </div>
            <InspectionTable
                inspections={inspections}
                onEdit={setEditingInspection}
                onDelete={setDeletingInspection}
            />
            {
                showModal && (
                    <AddInspectionModal
                        vehicles={vehicles}
                        onClose={() => setShowModal(false)}
                        onSave={handleSave}
                    />
                )
            }
            {
                editingInspection && (
                    <EditInspectionModal
                        inspection={editingInspection}
                        vehicles={vehicles}
                        onClose={() => setEditingInspection(null)}
                        onSave={handleUpdate}
                    />
                )
            }
            {
                deletingInspection && (
                    <DeleteConfirmModal
                        title="Delete Inspection"
                        message="Are you sure you want to delete this inspection?"
                        onCancel={() => setDeletingInspection(null)}
                        onConfirm={handleDelete}
                    />
                )
            }
        </div>
    );
}

export default Inspection;