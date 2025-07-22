import "./App.css";
import AgentProfile from "./components/AgentProfile";
import NavBar from "./components/Nav";
import "/assets/fonts/Space_Mono/SpaceMono-Regular.ttf";

function App() {
  // TODO :: Take this from user later
  const User = "Vivian";

  return (
    <div className="flex flex-col justify-around items-center h-screen w-full bg-gradient-to-b from-[#1c3638] via-[#162F30] to-[#112122] shadow-2xl ring-1 ring-white/5 shadow-black/30">
      <NavBar></NavBar>
      <AgentProfile />
      <h2
        className="text-center text-4xl text-white"
        style={{ fontFamily: "SpaceMono" }}
      >
        Hey {User}
      </h2>
      <div className="">
        {" "}
        <img
          className="rounded-full w-[100px] bg-[#0F584D]/80 hover:bg-[#0F584D]/65 border-2 border-emerald-800 hover:border-emerald-800/70 p-2 mt-10 mb-8"
          src="/assets/icons/mic_on.svg"
          alt="mic icon"
        ></img>
      </div>
    </div>
  );
}

export default App;
