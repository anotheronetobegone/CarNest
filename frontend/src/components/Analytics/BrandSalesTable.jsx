function BrandSalesTable({

    brands

}) {

    return (

        <table className="w-full bg-white rounded shadow mb-8">

            <thead>

                <tr className="bg-gray-100">

                    <th className="p-3 text-left">

                        Brand

                    </th>

                    <th className="p-3 text-left">

                        Sold

                    </th>

                    <th className="p-3 text-left">

                        Revenue

                    </th>

                    <th className="p-3 text-left">

                        Profit

                    </th>

                </tr>

            </thead>

            <tbody>

                {

                    brands.map((brand, index) => (

                        <tr key={index}>

                            <td className="p-3">

                                {brand.brand}

                            </td>

                            <td className="p-3">

                                {brand.vehicles_sold}

                            </td>

                            <td className="p-3">

                                ₹{brand.total_revenue}

                            </td>

                            <td className="p-3">

                                ₹{brand.total_profit}

                            </td>

                        </tr>

                    ))

                }

            </tbody>

        </table>

    );

}

export default BrandSalesTable;