import { useState } from "react";
import "./App.css";
import AgentProfile from "./components/AgentProfile";
import NavBar from "./components/Nav";
import "/assets/fonts/Space_Mono/SpaceMono-Regular.ttf";

function App() {
  // Take from user
  const User = "Vivian";
  const [isOn, setIsOn] = useState(false);

  async function micOn() {
    console.log("-- Turning Microphone On --");
    const res = await fetch("http://localhost:5000/agentcall", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input: "MIC_ON" }),
    });

    const data = await res.json();
    console.log(data);
  }

  async function micOff() {
    console.log("-- Turning Microphone Off --");
    const res = await fetch("http://localhost:5000/stoprecording", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input: "MIC_OFF" }),
    });

    const data = await res.json();
    console.log(data);
  }

  const toggleMic = async () => {
    if (isOn) {
      await micOff();
      setIsOn(false);
    } else {
      await micOn();
      setIsOn(true);
    }
  };

  return (
    <div
      className="flex flex-col justify-around items-center h-screen w-screen bg-gradient-to-b from-[#031825] via-[#001e33] to-[#001320] shadow-2xl ring-1 ring-white/5 shadow-black/40"
      style={{ fontFamily: "SpaceMono" }}
    >
      <NavBar />
      <AgentProfile />
      <h2
        className="text-center text-4xl text-sky-200 drop-shadow-md"
        style={{ fontFamily: "SpaceMono" }}
      >
        Hey {User}
      </h2>
      <div>
        {/* TODO :: change image to micoff onclick */}
        <img
          className="rounded-full w-[100px] bg-sky-800/70 hover:bg-sky-600/65 border-2 border-blue-500 hover:border-blue-400 p-2 mt-10 mb-8 transition"
          src={isOn ? "/assets/icons/mic_on.svg" : "/assets/icons/mic_off.svg"}
          alt="mic icon"
          onClick={toggleMic}
        />
      </div>
    </div>
  );
}

export default App;
