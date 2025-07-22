import "./App.css";
import AgentProfile from "./components/AgentProfile";
import NavBar from "./components/Nav";
import "/assets/fonts/Space_Mono/SpaceMono-Regular.ttf";

function App() {
  // Take from user
  const User = "Vivian";

  return (
    <div className="flex flex-col justify-around items-center h-screen w-full bg-gradient-to-b from-[#031825] via-[#001e33] to-[#001320] shadow-2xl ring-1 ring-white/5 shadow-black/40">
      <NavBar />
      <AgentProfile />
      <h2
        className="text-center text-4xl text-sky-200 drop-shadow-md"
        style={{ fontFamily: "SpaceMono" }}
      >
        Hey {User}
      </h2>
      <div>
        <img
          className="rounded-full w-[100px] bg-sky-800/70 hover:bg-sky-700/60 border-2 border-blue-500 hover:border-blue-400 p-2 mt-10 mb-8 transition"
          src="/assets/icons/mic_on.svg"
          alt="mic icon"
        />
      </div>
    </div>
  );
}

export default App;
