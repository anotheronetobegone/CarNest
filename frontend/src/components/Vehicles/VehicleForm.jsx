import { useState } from "react";

function VehicleForm({ initialData = {}, onSubmit, onCancel }) {
    const [form, setForm] = useState({
        brand: initialData.brand || "",
        model: initialData.model || "",
        year: initialData.year || "",
        fuel_type: initialData.fuel_type || "",
        transmission: initialData.transmission || "",
        color: initialData.color || "",
        mileage: initialData.mileage || "",
        purchase_price: initialData.purchase_price || "",
        selling_price: initialData.selling_price || "",
        status: initialData.status || "Available"
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

    return (
        <form onSubmit={handleSubmit} className="space-y-2">
            <input
                className="w-full border rounded p-2"
                name="brand"
                placeholder="Brand"
                value={form.brand}
                onChange={handleChange}
                required
            />
            <input
                className="w-full border rounded p-2"
                name="model"
                placeholder="Model"
                value={form.model}
                onChange={handleChange}
                required
            />
            <input
                className="w-full border rounded p-2"
                type="number"
                name="year"
                placeholder="Year"
                value={form.year}
                onChange={handleChange}
                required
            />
            <input
                className="w-full border rounded p-2"
                name="fuel_type"
                placeholder="Fuel Type"
                value={form.fuel_type}
                onChange={handleChange}
                required
            />
            <input
                className="w-full border rounded p-2"
                name="transmission"
                placeholder="Transmission"
                value={form.transmission}
                onChange={handleChange}
                required
            />
            <input
                className="w-full border rounded p-2"
                name="color"
                placeholder="Color"
                value={form.color}
                onChange={handleChange}
                required
            />
            <input
                className="w-full border rounded p-2"
                type="number"
                name="mileage"
                placeholder="Mileage"
                value={form.mileage}
                onChange={handleChange}
                required
            />
            <input
                className="w-full border rounded p-2"
                type="number"
                name="purchase_price"
                placeholder="Purchase Price"
                value={form.purchase_price}
                onChange={handleChange}
                required
            />
            <input
                className="w-full border rounded p-2"
                type="number"
                name="selling_price"
                placeholder="Selling Price"
                value={form.selling_price}
                onChange={handleChange}
            />
            <select
                className="w-full border rounded p-2"
                name="status"
                value={form.status}
                onChange={handleChange}
            >
                <option>Available</option>
                <option>Sold</option>
            </select>
            <div className="flex justify-end gap-3">
                <button
                    type="button"
                    onClick={onCancel}
                    className="px-4 py-2 border rounded"
                >
                    Cancel
                </button>
                <button
                    type="submit"
                    className="px-4 py-2 bg-blue-600 text-white rounded"
                >
                    Add Vehicle
                </button>
            </div>
        </form>
    );
}

export default VehicleForm;