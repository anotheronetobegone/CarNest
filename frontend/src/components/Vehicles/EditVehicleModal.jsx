import VehicleForm from "./VehicleForm";

function EditVehicleModal({ vehicle, onClose, onSave }) {
    return (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
            <div className="bg-white rounded-lg p-6 w-[500px]">
                <h2 className="text-2xl font-bold mb-5">
                    Edit Vehicle
                </h2>
                <VehicleForm
                    initialData={vehicle}
                    onSubmit={onSave}
                    onCancel={onClose}
                />
            </div>
        </div>
    );
}

export default EditVehicleModal;