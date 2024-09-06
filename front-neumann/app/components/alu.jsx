"use client"

export default function ALU({accumulator, r_entry}) {
    return (
        <section className="flex absolute flex-col min-w-[500px] min-h-[300px] bg-[#e2ffcf] right-96 top-20 border-[#7bed2f] border-2 z-30">
            <h1 className="ml-1">ALU</h1>
            <div className="flex flex-row w-full h-auto justify-center items-center mt-5">
                <div className="w-[150px] h-[130px] bg-[#7bed2f] skew-x-[-20deg] border-2 border-[#7bed2f] ml-5"></div>
                <div className="w-[150px] h-[130px] bg-[#7bed2f] skew-x-[20deg] border-2 border-[#7bed2f] mr-5"></div>
            </div>
            <div className="flex flex-row w-full h-auto justify-center items-center mt-5">
                <div className="flex flex-col w-1/2 h-auto justify-center items-center ml-5">
                    <span className="w-40 h-12 border-2 border-black bg-white flex flex-row justify-center items-center">{accumulator ? accumulator : ""}</span>
                    <h1>Accumulator</h1>
                </div>
                <div className="flex flex-col w-1/2 h-auto justify-center items-center mr-5">
                    <span className="w-40 h-12 border-2 border-black bg-white flex flex-row justify-center items-center">{r_entry ? r_entry : ""}</span>
                    <h1>R. Entry</h1>
                </div>
            </div>
        </section>
    )
}