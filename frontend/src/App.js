import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/Layout/Layout";

import Dashboard from "./pages/Dashboard";
import Vehicles from "./pages/Vehicles";
import Inspection from "./pages/Inspection";
import Sales from "./pages/Sales";
import Analytics from "./pages/Analytics";

function App() {
    return (
        <BrowserRouter>
            <Layout>
                <Routes>
                    <Route path="/" element={<Dashboard />} />
                    <Route path="/vehicles" element={<Vehicles />} />
                    <Route path="/inspection" element={<Inspection />} />
                    <Route path="/sales" element={<Sales />} />
                    <Route path="/analytics" element={<Analytics />} />
                </Routes>
            </Layout>
        </BrowserRouter>
    );
}

export default App;