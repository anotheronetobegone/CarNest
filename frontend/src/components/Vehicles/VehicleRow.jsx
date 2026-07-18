function VehicleRow({ vehicle }) {
    return (
        <tr className="border-b">
            <td className="p-3">{vehicle.brand}</td>
            <td className="p-3">{vehicle.model}</td>
            <td className="p-3">{vehicle.year}</td>
            <td className="p-3">{vehicle.mileage}</td>
            <td className="p-3">{vehicle.status}</td>
            <td className="p-3 space-x-2">
                <button className="text-blue-600">
                    Edit
                </button>
                <button className="text-red-600">
                    Delete
                </button>
            </td>
        </tr>
    );
}

export default VehicleRow;