import DashboardCards from "../components/Dashboard/DashboardCards";
import useDashboardApi from "../hooks/useDashboardApi";

function Dashboard() {

    const {
        dashboard,
        loading
    } = useDashboardApi();

    console.log(dashboard);

    if (loading) {
        return <h2>Loading...</h2>;
    }

    if (!dashboard) {
        return <h2>No dashboard data found.</h2>;
    }

    return (
        <DashboardCards data={dashboard} />
    );
    }

export default Dashboard;