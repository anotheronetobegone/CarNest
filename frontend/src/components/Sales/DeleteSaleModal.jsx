function DeleteSaleModal({
    onClose,
    onConfirm
}) {

    return (
        <div className="fixed inset-0 bg-black/50 flex justify-center items-center">
            <div className="bg-white rounded-lg p-6 w-[400px]">
                <h2 className="text-xl font-bold">
                    Delete Sale
                </h2>
                <p className="mt-3">
                    Are you sure you want to delete this sale?
                </p>
                <div className="flex justify-end gap-3 mt-6">
                    <button
                        onClick={onClose}
                        className="border px-4 py-2 rounded"
                    >
                        Cancel
                    </button>
                    <button
                        onClick={onConfirm}
                        className="bg-red-600 text-white px-4 py-2 rounded"
                    >
                        Delete
                    </button>
                </div>
            </div>
        </div>
    );
}

export default DeleteSaleModal;