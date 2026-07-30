"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { LayoutDashboard, Box, Settings } from "lucide-react";
import { cn } from "@/lib/utils";

export function Sidebar() {
  const pathname = usePathname();

  const links = [
    { name: "Marketplace", href: "/dashboard", icon: LayoutDashboard },
    { name: "Pipelines", href: "/pipeline", icon: Box },
    { name: "Text Processing", href: "/text-processing", icon: Box },
    { name: "Programming", href: "/programming", icon: Box },
    { name: "Settings", href: "/dashboard/settings", icon: Settings },
  ];

  return (
    <div className="w-64 border-r border-white/10 bg-black/50 backdrop-blur-md h-full flex flex-col p-4 shrink-0">
      <Link href="/" className="flex items-center gap-2 mb-8 px-2">
        <div className="w-8 h-8 rounded-lg bg-cyan-600 flex items-center justify-center">
          <Box className="w-5 h-5 text-white" />
        </div>
        <span className="font-bold text-lg tracking-tight">AgentVerse</span>
      </Link>

      <div className="flex flex-col gap-2">
        <div className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2 px-2">Navigation</div>
        {links.map((link) => {
          const isActive = pathname === link.href;
          return (
            <Link
              key={link.name}
              href={link.href}
              className={cn(
                "flex items-center gap-3 px-3 py-2 rounded-md transition-colors text-sm font-medium",
                isActive 
                  ? "bg-white/10 text-white" 
                  : "text-gray-400 hover:text-white hover:bg-white/5"
              )}
            >
              <link.icon className="w-4 h-4" />
              {link.name}
            </Link>
          );
        })}
      </div>
    </div>
  );
}
