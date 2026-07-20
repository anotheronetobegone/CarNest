import SummaryCard from "./SummaryCard";

function AnalyticsCards({

    dashboard

}) {

    return (

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 mb-8">

            <SummaryCard

                title="Revenue"

                value={`₹${dashboard?.total_revenue}`}

            />

            <SummaryCard

                title="Profit"

                value={`₹${dashboard?.total_profit}`}

            />

            <SummaryCard

                title="Vehicles"

                value={dashboard?.total_vehicles}

            />

            <SummaryCard

                title="Sold"

                value={dashboard?.sold_vehicles}

            />

        </div>

    );

}

export default AnalyticsCards;