import InspectionForm from "./InspectionForm";

function EditInspectionModal({
    inspection,
    vehicles,
    onClose,
    onSave
}) {
    return (
        <div className="fixed inset-0 bg-black/50 flex justify-center items-center">
            <div className="bg-white rounded-lg p-6 w-[500px]">
                <h2 className="text-2xl font-bold mb-5">
                    Edit Inspection
                </h2>
                <InspectionForm
                    initialData={inspection}
                    vehicles={vehicles}
                    onSubmit={onSave}
                    onCancel={onClose}
                />
            </div>
        </div>
    );
}

export default EditInspectionModal;