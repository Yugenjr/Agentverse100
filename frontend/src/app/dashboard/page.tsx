"use client";

import { useEffect, useState } from "react";
import { fetchAgents, fetchCategories, executeCategory, Agent, Category, AgentOutput } from "@/lib/api";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Play, Search, Loader2 } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { AgentModal } from "@/components/agent-modal";

export default function DashboardPage() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [search, setSearch] = useState("");
  const [activeCategory, setActiveCategory] = useState<string | null>(null);
  
  const [selectedAgent, setSelectedAgent] = useState<Agent | null>(null);
  
  const [runningCategory, setRunningCategory] = useState<string | null>(null);
  const [categoryResults, setCategoryResults] = useState<AgentOutput[] | null>(null);
  const [categoryTime, setCategoryTime] = useState<number | null>(null);

  useEffect(() => {
    fetchCategories().then(setCategories).catch(console.error);
  }, []);

  useEffect(() => {
    const delayDebounceFn = setTimeout(() => {
      fetchAgents(search).then(setAgents).catch(console.error);
    }, 300);
    return () => clearTimeout(delayDebounceFn);
  }, [search]);

  const filteredAgents = activeCategory 
    ? agents.filter(a => a.category === activeCategory)
    : agents;

  const handleRunCategory = async (catName: string) => {
    setRunningCategory(catName);
    setCategoryResults(null);
    setCategoryTime(null);
    try {
      const res = await executeCategory(catName, "Hello world, this is a test input for the entire category.");
      setCategoryResults(res.results);
      setCategoryTime(res.execution_time);
    } catch (e) {
      console.error(e);
    } finally {
      setRunningCategory(null);
    }
  };

  return (
    <div className="flex flex-col h-full gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Agent Marketplace</h1>
          <p className="text-gray-400">Discover and execute 100 specialized AI agents.</p>
        </div>
        <div className="relative w-72">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
          <Input 
            placeholder="Search agents..." 
            className="pl-9 bg-white/5 border-white/10 text-white"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>
      </div>

      <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-none">
        <Badge 
          variant={activeCategory === null ? "default" : "outline"}
          className="cursor-pointer px-4 py-1 text-sm shrink-0 bg-white/10 hover:bg-white/20 border-white/10"
          onClick={() => setActiveCategory(null)}
        >
          All
        </Badge>
        {categories.map((c) => (
          <Badge 
            key={c.name}
            variant={activeCategory === c.name ? "default" : "outline"}
            className="cursor-pointer px-4 py-1 text-sm shrink-0 border-white/10 flex items-center gap-2 hover:bg-white/10"
            onClick={() => setActiveCategory(c.name)}
            style={activeCategory === c.name ? { backgroundColor: 'rgb(8 145 178)', borderColor: 'rgb(8 145 178)', color: 'white' } : {}}
          >
            {c.name} <span className="opacity-50 text-xs">{c.count}</span>
          </Badge>
        ))}
      </div>

      {activeCategory && (
        <div className="flex items-center justify-between bg-white/5 p-4 rounded-xl border border-white/10">
          <div>
            <h3 className="font-semibold text-lg">{activeCategory}</h3>
            <p className="text-sm text-gray-400">Run all agents in this category concurrently.</p>
          </div>
          <Button 
            onClick={() => handleRunCategory(activeCategory)}
            disabled={runningCategory === activeCategory}
            className="bg-cyan-600 hover:bg-cyan-500"
          >
            {runningCategory === activeCategory ? <Loader2 className="w-4 h-4 animate-spin mr-2" /> : <Play className="w-4 h-4 mr-2" />}
            Run Category
          </Button>
        </div>
      )}

      {categoryResults && (
        <div className="bg-white/5 p-4 rounded-xl border border-white/10">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-semibold text-lg">Category Execution Results</h3>
            <Badge variant="outline" className="text-green-400 border-green-400/20 bg-green-400/10">
              Completed in {categoryTime}s
            </Badge>
          </div>
          <div className="space-y-4 max-h-64 overflow-y-auto pr-2">
            {categoryResults.map((res, i) => (
              <div key={i} className="p-3 bg-black/50 rounded-lg border border-white/5">
                <div className="flex justify-between items-center mb-2">
                  <span className="font-medium text-cyan-400">{res.agent_name}</span>
                  <span className="text-xs text-gray-500">{res.execution_time}s</span>
                </div>
                <p className="text-sm text-gray-300 line-clamp-2">{res.output}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 mt-8">
        <AnimatePresence>
          {filteredAgents.map((agent) => (
            <motion.div
              key={agent.name}
              layout
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.9 }}
              transition={{ duration: 0.2 }}
            >
              <Card 
                className="bg-white/5 border-white/10 hover:bg-white/10 transition-colors cursor-pointer h-full flex flex-col"
                onClick={() => setSelectedAgent(agent)}
              >
                <CardHeader>
                  <CardTitle className="text-lg text-white flex items-center justify-between">
                    {agent.name}
                  </CardTitle>
                  <CardDescription className="text-gray-400 mt-2 line-clamp-2">
                    {agent.description}
                  </CardDescription>
                </CardHeader>
                <div className="mt-auto p-6 pt-0">
                  <Badge variant="outline" className="text-cyan-400 border-cyan-400/20 bg-cyan-400/10">
                    {agent.category}
                  </Badge>
                </div>
              </Card>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>

      {selectedAgent && (
        <AgentModal agent={selectedAgent} onClose={() => setSelectedAgent(null)} />
      )}
    </div>
  );
}
