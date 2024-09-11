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
  const [messageError, setMessageError] = useState(null);
  const [x, setX] = useState(null);
  const [y, setY] = useState(null);
  const addX = (e) => {
    const newX = e.target.value;
    setX(newX);
  }
  const addY = (e) => {
    const newY = e.target.value;
    setY(newY);
  }
  const fetchServer = useServer();
  const initApp = () => {
    if (x && y) {
      fetchServer.mutate({x, y});
    }
  };
  useEffect(() => {
    if (fetchServer.isSuccess) {
      let res = fetchServer.data;
      if (res.length !== 0){
        setMessageError(null);
        setActualStep(0);
        setData(res);
      } else {
        setData(null);
        setActualStep(0);
        setMessageError("The numbers can't be added.");
      }
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
      <ControlUnit decoder={data ? data[actualStep].state.decoder : null} counter={data ? data[actualStep].state.counter : null} r_instructions={data ? data[actualStep].state.r_instructions : null} actualChange={data ? data[actualStep].actual_change : null}/>
      <ALU accumulator={data ? data[actualStep].state.accumulator : null} r_entry={data ? data[actualStep].state.r_entry : null} actualChange={data ? data[actualStep].actual_change : null}/>
      <Memory r_directions={data ? data[actualStep].state.r_directions : null} table_of_memory={data ? data[actualStep].state.table_of_memory : null} r_data={data ? data[actualStep].state.r_data : null} actualChange={data ? data[actualStep].actual_change : null}/>
      <Lines />
      <h1 className="flex flex-row w-auto h-auto left-12 text-2xl font-bold justify-center items-center z-50 absolute ml-1">VonNeumannCalculator</h1>
      <input type="number" className="flex flex-row w-32 h-auto left-12 bottom-96 justify-start items-center p-2 border-black border-2 z-50 absolute" onChange={(e) => addX(e)} min="0" max="255"/>
      <span className="flex flex-row w-auto h-auto left-44 text-4xl font-bold bottom-96 justify-center items-center z-50 absolute ml-1">+</span>
      <input type="number" className="flex flex-row w-32 h-auto left-52 bottom-96 justify-start items-center p-2 border-black border-2 z-50 absolute" onChange={(e) => addY(e)} min="0" max="255"/>
      <button className="flex flex-row w-32 h-auto left-32 bottom-80 justify-center font-bold items-center border-black border-2 rounded-xl bg-green-600 p-2 z-50 absolute" onClick={initApp}>Start</button>
      {data && <p className="flex flex-row w-72 h-auto left-12 bottom-36 justify-center items-center p-2 border-black border-2 bg-blue-400 z-50 absolute">{data[actualStep].description}</p>}
      {messageError && <p className="flex flex-row w-72 h-auto left-12 bottom-36 justify-center items-center p-2 border-black border-2 bg-blue-400 z-50 absolute">{data ? data[actualStep].description : messageError}</p>}
      {data && <button onClick={previousStep} className="flex flex-row w-32 h-8 bottom-24 left-12 absolute z-50 border-2 border-black rounded-xl bg-green-500 justify-center items-center">Previous Step</button>}
      {data && <button onClick={nextStep} className="flex flex-row w-32 h-8 bottom-24 left-52 absolute z-50 border-2 border-black rounded-xl bg-green-500 justify-center items-center">Next Step</button>}
    </main>
  );
}
