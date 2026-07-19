import { useState } from "react";

function SaleForm({
    vehicles,
    initialData = {},
    onSubmit,
    onCancel
}) {

    const [form, setForm] = useState({
        vehicle_id: initialData.vehicle_id || "",
        buyer_name: initialData.buyer_name || "",
        sale_date: initialData.sale_date || "",
        final_price: initialData.final_price || ""
    });

    function handleChange(e) {
        setForm({
            ...form,
            [e.target.name]: e.target.value
        });
    }

    function handleSubmit(e) {
        e.preventDefault();
        onSubmit(form);
    }

    const selectedVehicle = vehicles.find(
        vehicle => vehicle.vehicle_id === Number(form.vehicle_id)
    );

    return (
        <form
            onSubmit={handleSubmit}
            className="space-y-4"
        >
            <select
                name="vehicle_id"
                value={String(form.vehicle_id)}
                onChange={handleChange}
                className="w-full border rounded p-2"
                required
            >
                <option value="">
                    Select Vehicle
                </option>
                {
                    vehicles.map(vehicle => (
                        <option
                            key={vehicle.vehicle_id}
                            value={String(vehicle.vehicle_id)}
                        >
                            {vehicle.brand} {vehicle.model}
                        </option>
                    ))
                }
            </select>
            {
                selectedVehicle && (
                    <div className="text-sm text-gray-600">
                        Purchase Price :
                        ₹{selectedVehicle.purchase_price}
                    </div>
                )
            }
            <input
                type="text"
                name="buyer_name"
                placeholder="Buyer Name"
                value={form.buyer_name}
                onChange={handleChange}
                className="w-full border rounded p-2"
                required
            />
            <input
                type="date"
                name="sale_date"
                value={form.sale_date}
                onChange={handleChange}
                className="w-full border rounded p-2"
                required
            />
            <input
                type="number"
                name="final_price"
                placeholder="Final Price"
                value={form.final_price}
                onChange={handleChange}
                className="w-full border rounded p-2"
                required
            />
            <div className="flex justify-end gap-3">
                <button
                    type="button"
                    onClick={onCancel}
                    className="border px-4 py-2 rounded"
                >
                    Cancel
                </button>
                <button
                    type="submit"
                    className="bg-blue-600 text-white px-4 py-2 rounded"
                >
                    Save
                </button>
            </div>
        </form>
    );
}

export default SaleForm;