function Header() {

    return (
        <header className="bg-white shadow px-8 py-4 flex justify-between items-center">
            <div>
                <h1 className="text-2xl font-bold">
                    CarNest Dashboard
                </h1>
                <p className="text-gray-500">
                    Used Car Dealership Management
                </p>
            </div>
            <div>
                <div className="w-11 h-11 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold">
                    PR
                </div>
            </div>
        </header>
    );
}

export default Header;