export default function NavBar() {
  return (
    <div className="flex pt-6 mb-8 justify-between items-center w-[90%]">
      <div>
        <img
          className="w-[40px]"
          src="/assets/icons/sidebar.svg"
          alt="sidebar"
        />
      </div>
      <div>
        <h2 className="text-3xl text-sky-200 font-bold tracking-wide">Echo</h2>
      </div>
      <div>
        <img
          className="rounded-full w-[50px] border-2 border-transparent hover:border-sky-500/70"
          src="/profile.jpeg"
          alt="user profile image"
        />
      </div>
    </div>
  );
}
