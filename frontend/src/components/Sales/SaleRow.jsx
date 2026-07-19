function SaleRow({
    sale,
    onEdit,
    onDelete
}) {

    return (
        <tr className="border-b">
            <td className="p-3">
                {sale.vehicle_name}
            </td>
            <td className="p-3">
                {sale.buyer_name}
            </td>
            <td className="p-3">
                {sale.sale_date}
            </td>
            <td className="p-3">
                ₹{sale.final_price}
            </td>
            <td className="p-3 text-green-600 font-semibold">
                ₹{sale.profit}
            </td>
            <td className="p-3">
                <button
                    onClick={() => onEdit(sale)}
                    className="text-blue-600 mr-4"
                >
                    Edit
                </button>
                <button
                    onClick={() => onDelete(sale)}
                    className="text-red-600"
                >
                    Delete
                </button>
            </td>
        </tr>
    );
}

export default SaleRow;