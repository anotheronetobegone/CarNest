import VehicleRow from "./VehicleRow";

function VehicleTable({ vehicles, onEdit, onDelete }) {
    return (
        <table className="w-full bg-white shadow rounded">
            <thead className="bg-gray-100">
                <tr>
                    <th className="p-3 text-left">Brand</th>
                    <th className="p-3 text-left">Model</th>
                    <th className="p-3 text-left">Year</th>
                    <th className="p-3 text-left">Mileage</th>
                    <th className="p-3 text-left">Status</th>
                    <th className="p-3 text-left">Actions</th>
                </tr>
            </thead>
            <tbody>
                {vehicles.map(vehicle => (
                    <VehicleRow
                        key={vehicle.vehicle_id}
                        vehicle={vehicle}
                        onEdit={onEdit}
                        onDelete={onDelete}
                    />
                ))}
            </tbody>
        </table>
    );
}

export default VehicleTable;