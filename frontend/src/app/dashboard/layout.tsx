import { Sidebar } from "@/components/sidebar";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex flex-row w-full h-screen bg-black text-white overflow-hidden selection:bg-cyan-500/30">
      <div className="relative z-50 shrink-0">
        <Sidebar />
      </div>
      <main className="flex-1 min-w-0 overflow-y-auto overflow-x-hidden relative">
        {/* Subtle background glow */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-4xl h-96 bg-cyan-600/10 rounded-full blur-[128px] pointer-events-none" />
        
        <div className="relative z-10 p-8 h-full">
          {children}
        </div>
      </main>
    </div>
  );
}
