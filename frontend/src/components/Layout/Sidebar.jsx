import { NavLink } from "react-router-dom";

function Sidebar() {

    const menu = [
        {
            title: "Dashboard",
            path: "/"
        },
        {
            title: "Vehicles",
            path: "/vehicles"
        },
        {
            title: "Inspection",
            path: "/inspection"
        },
        {
            title: "Sales",
            path: "/sales"
        },
        {
            title: "Analytics",
            path: "/analytics"
        }
    ];

    return (

        <aside className="w-64 bg-slate-900 text-white">

            <div className="text-2xl font-bold p-6 border-b border-slate-700">
                CarNest
            </div>

            <nav className="mt-5">
                {menu.map((item) => (
                    <NavLink
                        key={item.title}
                        to={item.path}
                        className={({ isActive }) =>
                            `flex items-center gap-3 px-6 py-4 hover:bg-slate-700 transition ${
                                isActive ? "bg-blue-600" : ""
                            }`
                        }
                    >
                        {item.title}
                    </NavLink>
                ))}
            </nav>
        </aside>
    );
}

export default Sidebar;