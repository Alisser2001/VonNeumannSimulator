"use client";
import ControlUnit from "./components/controlUnit";
import ALU from "./components/alu";
import Memory from "./components/memory";
import Lines from "./components/lines";
import { useServer } from "../hooks/useServer";
import { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState(null);
  const [actualStep, setActualStep] = useState(0);
  const fetchServer = useServer();
  useEffect(() => {
    if (!data) {
      fetchServer.mutate();
    }
  }, []);
  useEffect(() => {
    if (fetchServer.isSuccess) {
      let res = fetchServer.data;
      setData(res);
    }
  }, [fetchServer.isSuccess]);
  const nextStep = () => {
    if(actualStep < data.length-1){
      setActualStep(actualStep+1);
    }
  }
  const previousStep = () => {
    if(actualStep > 0){
      setActualStep(actualStep-1);
    }
  }
  return (
    <main className="flex h-auto min-h-screen w-screen flex-col items-center justify-center bg-white fixed">
      <ControlUnit decoder={data ? data[actualStep].state.decoder : null} counter={data ? data[actualStep].state.counter : null} r_instructions={data ? data[actualStep].state.r_instructions : null} />
      <ALU accumulator={data ? data[actualStep].state.accumulator : null} r_entry={data ? data[actualStep].state.r_entry : null} />
      <Memory r_directions={data ? data[actualStep].state.r_directions : null} table_of_memory={data ? data[actualStep].state.table_of_memory : null} r_data={data ? data[actualStep].state.r_data : null} />
      <Lines />
      {data && <p className="flex flex-row w-64 h-auto left-12 top-32 justify-center items-center p-2 border-black border-2 bg-blue-400 z-50 absolute">{data[actualStep].description}</p>}
      <button onClick={previousStep} className="flex flex-row w-32 h-8 left-32 bottom-32 absolute z-50 border-2 border-black rounded-xl bg-green-500 justify-center items-center">Previous Step</button>
      <button onClick={nextStep} className="flex flex-row w-32 h-8 right-32 bottom-32 absolute z-50 border-2 border-black rounded-xl bg-green-500 justify-center items-center">Next Step</button>
    </main>
  );
}
