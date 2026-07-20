import useAnalytics from "../hooks/useAnalytics";

import AnalyticsCards from "../components/Analytics/AnalyticsCards";

import BrandSalesTable from "../components/Analytics/BrandSalesTable";

import MonthlySalesTable from "../components/Analytics/MonthlySalesTable";

function Analytics() {

    const {

        dashboard,

        brands,

        monthlySales,

        loading

    } = useAnalytics();

    if (loading)

        return <h2>Loading...</h2>;

    console.log(dashboard);

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">

                Analytics

            </h1>

            <AnalyticsCards

                dashboard={dashboard}

            />

            <h2 className="text-xl font-semibold mb-3">

                Brand Sales

            </h2>

            <BrandSalesTable

                brands={brands}

            />

            <h2 className="text-xl font-semibold mb-3">

                Monthly Sales

            </h2>

            <MonthlySalesTable

                monthlySales={monthlySales}

            />

        </div>

    );

}

export default Analytics;