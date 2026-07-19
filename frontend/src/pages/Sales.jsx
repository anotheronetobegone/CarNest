import { useState } from "react";
import SaleTable from "../components/Sales/SaleTable";
import useSales from "../hooks/useSales";
import useVehicles from "../hooks/useVehicles";
import { createSale, deleteSale, updateSale } from "../services/api";
import EditSaleModal from "../components/Sales/EditSaleModal";
import AddSaleModal from "../components/Sales/AddSaleModal";
import DeleteSaleModal from "../components/Sales/DeleteSaleModal";
import useSaleVehicles from "../hooks/useSaleVehicles";

function Sales() {
    const {
        sales,
        loading,
        reload
    } = useSales();

    const {vehicles} = useVehicles();
    const saleVehicles = useSaleVehicles();

    const [showModal, setShowModal] = useState(false);
    const [editingSale, setEditingSale] = useState(null);
    const [deletingSale, setDeletingSale] = useState(null);

    if (loading)
        return <h2>Loading...</h2>;

    async function handleSave(data) {
        await createSale(data);
        reload();
        setShowModal(false);
    }

    async function handleUpdate(data) {
        await updateSale(
            editingSale.sale_id,
            data
        );
        reload();
        setEditingSale(null);
    }

    async function handleDelete() {
        await deleteSale(
            deletingSale.sale_id
        );
        reload();
        setDeletingSale(null);
    }
        
    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold">
                    Sales
                </h1>
                <button
                    onClick={() => setShowModal(true)}
                    className="bg-blue-600 text-white px-4 py-2 rounded"
                >
                    + New Sale
                </button>
            </div>
            <SaleTable
                sales={sales}
                onEdit={setEditingSale}
                onDelete={setDeletingSale}
            />
            {
                showModal && (
                    <AddSaleModal
                        vehicles={saleVehicles}
                        onClose={() => setShowModal(false)}
                        onSave={handleSave}
                    />
                )
            }
            {
                editingSale && (
                    <EditSaleModal
                        sale={editingSale}
                        vehicles={vehicles}
                        onClose={() => setEditingSale(null)}
                        onSave={handleUpdate}
                    />
                )
            }
            {
                deletingSale && (
                    <DeleteSaleModal
                        onClose={() => setDeletingSale(null)}
                        onConfirm={handleDelete}
                    />
                )
            }
        </div>
    );
}

export default Sales;