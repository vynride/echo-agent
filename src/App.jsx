import "./App.css";
import AgentProfile from "./components/AgentProfile";
import NavBar from "./components/Nav";
import "./assets/fonts/Space_Mono/SpaceMono-Regular.ttf";

function App() {
  // TODO :: Take this from user later
  const User = "Vivian";

  return (
    <>
      <div className="flex flex-col justify-around items-center">
        <NavBar></NavBar>
        <AgentProfile />
        <h2 className="text-center text-4xl text-emerald-100" style={{ fontFamily: "SpaceMono" }}>Hey {User}</h2>
      </div>
    </>
  );
}

export default App;
