"use client"

export default function Memory({r_directions, table_of_memory, r_data}) {
    return (
        <section className="flex absolute flex-row min-w-[800px] min-h-[400px] bg-[#ffe8cf] bottom-32 border-[#fa992f] border-2 z-30 flex-wrap items-start">
            <h1 className="ml-1 h-5 w-full">Memory</h1>
            <div className="flex flex-col w-1/3 h-auto justify-center items-center">
                <span className="w-40 h-12 border-2 border-black bg-white flex flex-row justify-center items-center">{r_directions ? r_directions : ""}</span>
                <h1>R. Directions</h1>
            </div>
            <div className="flex flex-col w-1/3 h-auto justify-center items-center">
                <h1>Table of Memory</h1>
                <table className="flex w-full h-auto flex-col border-black border-2">
                    <thead className="w-full">
                        <tr className="w-full border-b-2 border-black bg-[#fa992f]">
                            <th className="w-[104px] border-r-2 border-black">Direction</th>
                            <th className="w-[160px]">Content</th>
                        </tr>
                    </thead>
                    <tbody className="w-full">
                        <tr className="w-full border-b-2 border-black">
                            <td className="w-[104px] text-center border-r-2 border-black">0000</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["0000"] : "00000000"}</td>
                        </tr>
                        <tr className="w-full border-b-2 border-black">
                            <td className="w-[104px] text-center border-r-2 border-black">0001</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["0001"] : "00000000"}</td>
                        </tr>
                        <tr className="w-full border-b-2 border-black">
                            <td className="w-[104px] text-center border-r-2 border-black">0010</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["0010"] : "00000000"}</td>
                        </tr>
                        <tr className="w-full border-b-2 border-black">
                            <td className="w-[104px] text-center border-r-2 border-black">0011</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["0011"] : "00000000"}</td>
                        </tr>
                        <tr className="w-full border-b-2 border-black">
                            <td className="w-[104px] text-center border-r-2 border-black">0100</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["0100"] : "00000000"}</td>
                        </tr>
                        <tr className="w-full border-b-2 border-black">
                            <td className="w-[104px] text-center border-r-2 border-black">0101</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["0101"] : "00000000"}</td>
                        </tr>
                        <tr className="w-full border-b-2 border-black">
                            <td className="w-[104px] text-center border-r-2 border-black">0110</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["0110"] : "00000000"}</td>
                        </tr>
                        <tr className="w-full border-b-2 border-black">
                            <td className="w-[104px] text-center border-r-2 border-black">0111</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["0111"] : "00000000"}</td>
                        </tr>
                        <tr className="w-full">
                            <td className="w-[104px] text-center border-r-2 border-black">1000</td>
                            <td className="w-[160px] text-center">{table_of_memory ? table_of_memory["1000"] : "00000000"}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div className="flex flex-col w-1/3 h-auto justify-center items-center">
                <span className="w-40 h-12 border-2 border-black bg-white flex flex-row justify-center items-center">{r_data ? r_data : ""}</span>
                <h1>R. Data</h1>
            </div>
        </section>
    )
}