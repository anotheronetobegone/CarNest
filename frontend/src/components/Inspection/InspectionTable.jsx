import InspectionRow from "./InspectionRow";

function InspectionTable({
    inspections,
    onEdit,
    onDelete
}) {
    return (
        <table className="w-full bg-white shadow rounded">
            <thead className="bg-gray-100">
                <tr>
                    <th className="p-3 text-left">
                        Vehicle
                    </th>
                    <th className="p-3 text-left">
                        Date
                    </th>
                    <th className="p-3 text-left">
                        Condition
                    </th>
                    <th className="p-3 text-left">
                        Status
                    </th>
                    <th className="p-3 text-left">
                        Actions
                    </th>
                </tr>
            </thead>
            <tbody>
                {inspections.map(inspection => (
                    <InspectionRow
                        key={inspection.inspection_id}
                        inspection={inspection}
                        onEdit={onEdit}
                        onDelete={onDelete}
                    />
                ))}
            </tbody>
        </table>
    );
}

export default InspectionTable;