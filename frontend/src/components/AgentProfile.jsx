export default function AgentProfile() {
  return (
    <div className="flex items-center justify-center m-8">
      <div className="relative group">
        <div
          className="absolute inset-0 rounded-full 
          bg-gradient-to-br from-emerald-700/30 via-teal-500/20 to-cyan-700/10 
          blur-2xl opacity-70 
          group-hover:opacity-90 
          transition duration-300"
        ></div>

        <div
          className="relative z-10 rounded-full 
          bg-[#0C6455]/70 
          w-[250px] h-[250px] 
          border border-emerald-400/25 
          shadow-[0_0_40px_rgba(20,90,80,0.5)] 
          ring-1 ring-white/10 
          backdrop-blur-md 
          transition-all duration-300 
          group-hover:shadow-[0_0_70px_rgba(50,160,120,0.8)] group-hover:scale-105"
        >
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="w-24 h-24 rounded-full bg-emerald-900/40 blur-lg"></div>
          </div>
        </div>
      </div>
    </div>
  );
}
