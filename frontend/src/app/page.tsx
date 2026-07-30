"use client";

import { motion } from "framer-motion";
import { ArrowRight, Box, Cpu, Zap } from "lucide-react";
import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-black text-white selection:bg-cyan-500/30 overflow-hidden flex flex-col items-center justify-center relative">
      {/* Background gradients */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-cyan-600/20 rounded-full blur-[128px]" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-600/20 rounded-full blur-[128px]" />
      
      <main className="z-10 flex flex-col items-center text-center px-4 max-w-5xl">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-sm mb-8">
            <Zap className="w-4 h-4 text-cyan-400" />
            <span className="text-gray-300">Powered by Groq</span>
          </div>
        </motion.div>

        <motion.h1 
          className="text-6xl md:text-8xl font-bold tracking-tighter bg-clip-text text-transparent bg-gradient-to-br from-white to-gray-500 mb-6"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.1 }}
        >
          AgentVerse-100
        </motion.h1>

        <motion.p 
          className="text-xl text-gray-400 max-w-2xl mb-10"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
        >
          A sprawling marketplace of exactly 100 specialized AI agents. Browse, execute, and chain them into powerful automated pipelines.
        </motion.p>

        <motion.div
          className="flex gap-4"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.3 }}
        >
          <Link href="/dashboard">
            <Button size="lg" className="h-12 px-8 bg-cyan-600 hover:bg-cyan-500 text-white rounded-full text-base">
              Explore Agents <ArrowRight className="ml-2 w-4 h-4" />
            </Button>
          </Link>
          <Link href="/pipeline">
            <Button size="lg" variant="outline" className="h-12 px-8 rounded-full text-base bg-white/5 border-white/10 hover:bg-white/10">
              Build Pipeline <Box className="ml-2 w-4 h-4" />
            </Button>
          </Link>
        </motion.div>

        <motion.div 
          className="mt-24 grid grid-cols-1 md:grid-cols-3 gap-6"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.5 }}
        >
          {[
            { title: "100 Specialized Agents", desc: "Divided across 10 diverse categories.", icon: Cpu },
            { title: "Lightning Fast", desc: "Powered by Groq's high-speed inference.", icon: Zap },
            { title: "Pipeline Builder", desc: "Chain agents sequentially for complex tasks.", icon: Box },
          ].map((feature, idx) => (
            <div key={idx} className="p-6 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-sm flex flex-col items-center text-center">
              <feature.icon className="w-8 h-8 text-cyan-400 mb-4" />
              <h3 className="font-semibold text-lg mb-2">{feature.title}</h3>
              <p className="text-gray-400 text-sm">{feature.desc}</p>
            </div>
          ))}
        </motion.div>
      </main>
    </div>
  );
}
