import ControlUnit from "./components/controlUnit";
import ALU from "./components/alu";
import Memory from "./components/memory";
import Lines from "./components/lines";

export default function Home() {
  return (
    <main className="flex h-auto min-h-screen w-screen flex-col items-center justify-center bg-white fixed">
        <ControlUnit/>
        <ALU/>
        <Memory/>
        <Lines/>
    </main>
  );
}
