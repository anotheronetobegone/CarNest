import SaleForm from "./SaleForm";

function EditSaleModal({
    sale,
    vehicles,
    onClose,
    onSave
}) {
    return (
        <div className="fixed inset-0 bg-black/50 flex justify-center items-center">
            <div className="bg-white rounded-lg p-6 w-[500px]">
                <h2 className="text-2xl font-bold mb-5">
                    Edit Sale
                </h2>
                <SaleForm
                    vehicles={vehicles}
                    initialData={sale}
                    onSubmit={onSave}
                    onCancel={onClose}
                />
            </div>
        </div>
    );
}

export default EditSaleModal;