import SaleRow from "./SaleRow";

function SaleTable({
    sales,
    onEdit,
    onDelete
}) {

    return (
        <table className="w-full bg-white rounded shadow">
            <thead className="bg-gray-100">
                <tr>
                    <th className="p-3 text-left">Vehicle</th>
                    <th className="p-3 text-left">Buyer</th>
                    <th className="p-3 text-left">Sale Date</th>
                    <th className="p-3 text-left">Price</th>
                    <th className="p-3 text-left">Profit</th>
                    <th className="p-3 text-left">Actions</th>
                </tr>
            </thead>
            <tbody>
                {
                    sales.map(sale => (
                        <SaleRow
                            key={sale.sale_id}
                            sale={sale}
                            onEdit={onEdit}
                            onDelete={onDelete}
                        />
                    ))
                }
            </tbody>
        </table>
    );
}

export default SaleTable;