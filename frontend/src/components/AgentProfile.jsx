export default function AgentProfile() {
  return (
    <div className="flex items-center justify-center m-8">
      <div className="relative group">
        <div
          className="absolute inset-0 rounded-full 
            bg-gradient-to-br from-blue-700/30 via-cyan-500/20 to-sky-700/10 
            blur-2xl opacity-80 
            group-hover:opacity-100 
            transition duration-300"
        ></div>

        <div
          className="relative z-10 rounded-full 
            w-[250px] h-[250px] 
            border border-sky-400/20 
            shadow-[0_0_60px_rgba(80,180,255,0.3)] 
            ring-1 ring-white/10 
            backdrop-blur-md 
            transition-all duration-300 
            group-hover:shadow-[0_0_90px_rgba(80,180,255,0.5)] group-hover:scale-105"
          style={{
            backgroundImage: `
              radial-gradient(circle at center, #0a2a48 0%, transparent 25%),
              radial-gradient(circle at center, #0e3c6a 35%, transparent 55%),
              radial-gradient(circle at center, #14589b 65%, transparent 85%),
              radial-gradient(circle at center, #1b75d0 95%, transparent 100%)
            `,
            backgroundBlendMode: 'normal'
          }}
        >
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="w-20 h-20 rounded-full bg-sky-400/40 blur-md"></div>
            <div className="absolute w-32 h-32 rounded-full border border-sky-400/30 animate-ping"></div>
          </div>
        </div>
      </div>
    </div>
  );
}
