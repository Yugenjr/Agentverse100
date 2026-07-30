"use client";

import { useState, useEffect } from "react";
import { Agent, fetchAgents, executePipeline, PipelineNode, PipelineExecutionResult } from "@/lib/api";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Loader2, Plus, Play, ArrowDown, Trash2 } from "lucide-react";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Badge } from "@/components/ui/badge";
import { motion, AnimatePresence } from "framer-motion";

export default function PipelinePage() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [pipeline, setPipeline] = useState<Agent[]>([]);
  const [initialInput, setInitialInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PipelineExecutionResult | null>(null);

  useEffect(() => {
    fetchAgents().then(setAgents).catch(console.error);
  }, []);

  const addNode = (agentName: string) => {
    const agent = agents.find(a => a.name === agentName);
    if (agent) {
      setPipeline([...pipeline, agent]);
    }
  };

  const removeNode = (index: number) => {
    const newPipeline = [...pipeline];
    newPipeline.splice(index, 1);
    setPipeline(newPipeline);
  };

  const handleRun = async () => {
    if (!initialInput || pipeline.length === 0) return;
    setLoading(true);
    setResult(null);
    try {
      const nodes: PipelineNode[] = pipeline.map(a => ({ agent_name: a.name }));
      const res = await executePipeline(initialInput, nodes);
      setResult(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full gap-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Pipeline Builder</h1>
        <p className="text-gray-400">Chain multiple specialized agents together sequentially.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 h-full min-h-0">
        {/* Left Column: Builder */}
        <div className="flex flex-col gap-6 overflow-y-auto pr-2 pb-20">
          <div className="space-y-2">
            <label className="text-sm font-medium text-gray-300">1. Initial Input</label>
            <Textarea 
              placeholder="Provide the starting input for the pipeline..."
              className="bg-white/5 border-white/10 text-white min-h-[100px]"
              value={initialInput}
              onChange={(e) => setInitialInput(e.target.value)}
            />
          </div>

          <div className="space-y-4">
            <label className="text-sm font-medium text-gray-300 flex items-center justify-between">
              <span>2. Execution Sequence</span>
            </label>
            
            <AnimatePresence>
              {pipeline.map((agent, i) => (
                <motion.div
                  key={`${agent.name}-${i}`}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  className="relative"
                >
                  <Card className="bg-white/5 border-white/10 flex items-center justify-between p-4">
                    <div className="flex items-center gap-4">
                      <div className="w-8 h-8 rounded-full bg-cyan-600/20 text-cyan-400 flex items-center justify-center font-bold">
                        {i + 1}
                      </div>
                      <div>
                        <h4 className="font-semibold text-white">{agent.name}</h4>
                        <p className="text-xs text-gray-400">{agent.category}</p>
                      </div>
                    </div>
                    <Button variant="ghost" size="icon" className="text-red-400 hover:text-red-300 hover:bg-red-400/10" onClick={() => removeNode(i)}>
                      <Trash2 className="w-4 h-4" />
                    </Button>
                  </Card>
                  {i < pipeline.length - 1 && (
                    <div className="flex justify-center my-2 text-white/20">
                      <ArrowDown className="w-6 h-6" />
                    </div>
                  )}
                </motion.div>
              ))}
            </AnimatePresence>

            <div className="flex gap-2">
              <Select onValueChange={addNode}>
                <SelectTrigger className="w-full bg-white/5 border-white/10">
                  <SelectValue placeholder="Add an agent to the pipeline..." />
                </SelectTrigger>
                <SelectContent className="bg-zinc-900 border-white/10">
                  {agents.map(a => (
                    <SelectItem key={a.name} value={a.name} className="text-white">
                      {a.name} ({a.category})
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
          </div>

          <Button 
            size="lg"
            onClick={handleRun} 
            disabled={loading || !initialInput || pipeline.length === 0}
            className="w-full bg-cyan-600 hover:bg-cyan-500 mt-4"
          >
            {loading ? <Loader2 className="w-5 h-5 mr-2 animate-spin" /> : <Play className="w-5 h-5 mr-2" />}
            Run Pipeline
          </Button>
        </div>

        {/* Right Column: Results */}
        <div className="flex flex-col gap-4 bg-white/5 p-6 rounded-xl border border-white/10 h-full overflow-y-auto">
          <h3 className="font-semibold text-xl">Execution Results</h3>
          
          {!result && !loading && (
            <div className="flex-1 flex items-center justify-center text-gray-500 text-sm">
              Run the pipeline to see results here.
            </div>
          )}

          {loading && (
            <div className="flex-1 flex flex-col items-center justify-center text-cyan-400 space-y-4">
              <Loader2 className="w-12 h-12 animate-spin" />
              <p>Executing pipeline...</p>
            </div>
          )}

          {result && (
            <div className="space-y-6">
              <div className="flex items-center justify-between bg-black/50 p-4 rounded-lg border border-white/5">
                <span className="font-medium text-gray-300">Total Execution Time</span>
                <Badge variant="outline" className="text-green-400 border-green-400/20 bg-green-400/10">
                  {result.total_execution_time}s
                </Badge>
              </div>

              <div className="space-y-4">
                <h4 className="font-semibold text-gray-300">Step-by-Step Breakdown</h4>
                {result.steps.map((step, i) => (
                  <div key={i} className="bg-black/50 border border-white/5 rounded-lg p-4">
                    <div className="flex justify-between items-center mb-2">
                      <div className="flex items-center gap-2">
                        <Badge variant="secondary" className="bg-white/10 text-white">Step {i + 1}</Badge>
                        <span className="font-semibold text-cyan-400">{step.agent_name}</span>
                      </div>
                      <span className="text-xs text-gray-500">{step.execution_time}s</span>
                    </div>
                    <div className="text-sm text-gray-300 font-mono whitespace-pre-wrap max-h-48 overflow-y-auto bg-black p-3 rounded mt-3">
                      {step.output}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
