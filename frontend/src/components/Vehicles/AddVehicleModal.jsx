import VehicleForm from "./VehicleForm";

function AddVehicleModal({ onClose, onSave }) {
    return (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
            <div className="bg-white rounded-lg p-6 w-[500px]">
                <h2 className="text-2xl font-bold mb-5">
                    Add Vehicle
                </h2>
                <VehicleForm
                    onSubmit={onSave}
                    onCancel={onClose}
                />
            </div>
        </div>
    );
}

export default AddVehicleModal;