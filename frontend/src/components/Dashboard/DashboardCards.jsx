import StatCard from "./StatCard";

function DashboardCards({ data }) {
    console.log("DashboardCards data:", data);
    
    return (
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
            <StatCard
                title="Vehicles"
                value={data.total_vehicles}
                color="#2563eb"
            />
            <StatCard
                title="Revenue"
                value={`₹${data.total_revenue}`}
                color="#16a34a"
            />
            <StatCard
                title="Profit"
                value={`₹${data.total_profit}`}
                color="#f97316"
            />
            <StatCard
                title="Sold Cars"
                value={data.sold_vehicles}
                color="#9333ea"
            />
        </div>
    );
}

export default DashboardCards;