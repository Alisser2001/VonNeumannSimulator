"use client"

export default function ControlUnit() {
    return (
        <section className="flex absolute flex-row w-[500px] h-[300px] bg-[#daeaf5] left-96 top-20 border-[#32a8fa] border-2 z-30 flex-wrap">
            <h1 className="ml-1 h-5 w-full">Control Unit</h1>
            <div className="flex flex-col w-1/2 h-[280px] justify-center items-center">
                <span className="w-32 h-32 border-2 border-black bg-white"></span>
                <h1>Decoder</h1>
            </div>
            <div className="flex flex-col w-1/2 h-[280px] justify-center items-center">
                <div className="flex flex-col w-full h-[140px] justify-center items-center">
                    <span className="w-40 h-12 border-2 border-black bg-white"></span>
                    <h1>Counter</h1>
                </div>
                <div className="flex flex-col w-full h-[140px] justify-center items-center">
                    <span className="w-40 h-12 border-2 border-black bg-white"></span>
                    <h1>R. Instructions</h1>
                </div>
            </div>
        </section>
    )
}