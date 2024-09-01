"use client"

export default function Memory() {
    return (
        <section className="flex absolute flex-row min-w-[800px] min-h-[400px] bg-[#ffe8cf] bottom-32 border-[#fa992f] border-2 z-30 flex-wrap items-start">
            <h1 className="ml-1 h-5 w-full">Memory</h1>
            <div className="flex flex-col w-1/3 h-auto justify-center items-center">
                <span className="w-40 h-12 border-2 border-black bg-white"></span>
                <h1>R. Directions</h1>
            </div>
            <div className="flex flex-col w-1/3 h-auto justify-center items-center">
                <h1>Table of Memory</h1>
                <table className="flex w-full h-auto flex-col border-black border-2">
                    <tr className="w-full border-b-2 border-black bg-[#fa992f]">
                        <th className="w-[100px] border-r-2 border-black">Direction</th>
                        <th className="w-[160px]">Content</th>
                    </tr>
                    <tr className="w-full border-b-2 border-black">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                    <tr className="w-full border-b-2 border-black">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                    <tr className="w-full border-b-2 border-black">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                    <tr className="w-full border-b-2 border-black">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                    <tr className="w-full border-b-2 border-black">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                    <tr className="w-full border-b-2 border-black">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                    <tr className="w-full border-b-2 border-black">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                    <tr className="w-full border-b-2 border-black">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                    <tr className="w-full">
                        <td className="w-[100px] text-center border-r-2 border-black">0000</td>
                        <td className="w-[160px] text-center">00000000</td>
                    </tr>
                </table>
            </div>
            <div className="flex flex-col w-1/3 h-auto justify-center items-center">
                <span className="w-40 h-12 border-2 border-black bg-white"></span>
                <h1>R. Data</h1>
            </div>
        </section>
    )
}