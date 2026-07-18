function InspectionRow({ inspection, onEdit, onDelete }) {
    return (
        <tr className="border-b">
            <td className="p-3">
                {inspection.vehicle_name}
            </td>
            <td className="p-3">
                {inspection.inspection_date}
            </td>
            <td className="p-3">
                {inspection.condition}
            </td>
            <td className="p-3">
                <span
                    className={`px-3 py-1 rounded-full text-sm font-medium ${
                        inspection.status === "Passed"
                            ? "bg-green-100 text-green-700"
                            : inspection.status === "Pending"
                            ? "bg-yellow-100 text-yellow-700"
                            : "bg-red-100 text-red-700"
                    }`}
                >
                    {inspection.status}
                </span>
            </td>
            <td className="p-3 space-x-2">
                <button
                    className="text-blue-600"
                    onClick={() => onEdit(inspection)}
                >
                    Edit
                </button>
                <button
                    className="text-red-600"
                    onClick={() => onDelete(inspection)}
                >
                    Delete
                </button>
            </td>
        </tr>
    );
}

export default InspectionRow;