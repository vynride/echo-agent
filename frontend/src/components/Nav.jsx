export default function NavBar() {
  return (
    <div className="flex pt-6 mb-8 justify-between items-center w-[90%]">
      <div className="">
        {" "}
        <img
          className="w-[40px]"
          src="/assets/icons/sidebar.svg"
          alt="sidebar"
        ></img>
      </div>
      <div className="">
        {" "}
        <h2 className="text-3xl text-zinc-300">Echo</h2>
      </div>
      <div>
        {" "}
        <img
          className="rounded-full w-[50px] border-2 border-transparent hover:border-[#094939]/70"
          src="/profile.jpeg"
          alt="user profile image"
        ></img>
      </div>
    </div>
  );
}
