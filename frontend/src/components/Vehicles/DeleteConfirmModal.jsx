function DeleteConfirmModal({
    title,
    message,
    onConfirm,
    onCancel
}) {
    return (
        <div className="fixed inset-0 bg-black/40 flex justify-center items-center">
            <div className="bg-white rounded-lg shadow-lg w-[420px] p-6">
                <h2 className="text-xl font-bold mb-3">
                    {title}
                </h2>
                <p className="text-gray-600 mb-6">
                    {message}
                </p>
                <div className="flex justify-end gap-3">
                    <button
                        onClick={onCancel}
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

export default DeleteConfirmModal;