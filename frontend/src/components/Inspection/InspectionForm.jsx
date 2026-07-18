import { useState } from "react";

function InspectionForm({
    vehicles,
    initialData = {},
    onSubmit,
    onCancel
}) {

    const [form, setForm] = useState({

        vehicle_id: initialData.vehicle_id || "",

        inspection_date: initialData.inspection_date || "",

        condition: initialData.condition || "",

        remarks: initialData.remarks || "",

        status: initialData.status || "Pending"

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
        <form
            onSubmit={handleSubmit}
            className="space-y-2"
        >
            <select
                name="vehicle_id"
                value={form.vehicle_id}
                onChange={handleChange}
                className="w-full border rounded p-2"
                required
            >
                <option value="">
                    Select Vehicle
                </option>
                {vehicles.map(vehicle => (
                    <option
                        key={vehicle.vehicle_id}
                        value={vehicle.vehicle_id}
                    >
                        {vehicle.brand} {vehicle.model}
                    </option>
                ))}
            </select>
            <input
                type="date"
                name="inspection_date"
                value={form.inspection_date}
                onChange={handleChange}
                className="w-full border rounded p-2"
                required
            />
            <input
                type="text"
                name="condition"
                value={form.condition}
                onChange={handleChange}
                placeholder="Condition"
                className="w-full border rounded p-2"
                required
            />
            <textarea
                name="remarks"
                value={form.remarks}
                onChange={handleChange}
                placeholder="Remarks"
                className="w-full border rounded p-2"
            />
            <select
                name="status"
                value={form.status}
                onChange={handleChange}
                className="w-full border rounded p-2"
            >
                <option value="Pending">
                    Pending
                </option>
                <option value="Passed">
                    Passed
                </option>
                <option value="Failed">
                    Failed
                </option>
            </select>
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

export default InspectionForm;