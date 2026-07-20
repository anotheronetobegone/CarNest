function MonthlySalesTable({

    monthlySales

}) {

    return (

        <table className="w-full bg-white rounded shadow">

            <thead>

                <tr className="bg-gray-100">

                    <th className="p-3 text-left">

                        Month

                    </th>

                    <th className="p-3 text-left">

                        Sales

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

                    monthlySales.map((month) => (

                        <tr key={month.month}>

                            <td className="p-3">

                                {month.month}

                            </td>

                            <td className="p-3">

                                {month.sales}

                            </td>

                            <td className="p-3">

                                ₹{month.revenue}

                            </td>

                            <td className="p-3">

                                ₹{month.profit}

                            </td>

                        </tr>

                    ))

                }

            </tbody>

        </table>

    );

}

export default MonthlySalesTable;