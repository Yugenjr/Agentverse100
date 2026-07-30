"use client";

import { useEffect, useState } from "react";
import { Agent, AgentOutput } from "@/lib/api";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Play, Loader2, ArrowLeft } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { AgentModal } from "@/components/agent-modal";
import Link from "next/link";

export default function DataSciencePage() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [selectedAgent, setSelectedAgent] = useState<Agent | null>(null);
  const [runningAll, setRunningAll] = useState(false);
  const [categoryResults, setCategoryResults] = useState<AgentOutput[] | null>(null);
  const [categoryTime, setCategoryTime] = useState<number | null>(null);

  useEffect(() => {
    const fetchDSAgents = async () => {
      try {
        const res = await fetch("http://localhost:8000/api/agents/datascience");
        if (!res.ok) throw new Error("Failed to fetch data science agents");
        const data = await res.json();
        setAgents(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchDSAgents();
  }, []);

  const handleRunAll = async () => {
    setRunningAll(true);
    setCategoryResults(null);
    setCategoryTime(null);
    try {
      const res = await fetch("http://localhost:8000/api/execute/datascience/run-all", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            dataset_description: "Customer Churn Prediction Dataset containing demographics, account info, and churn status.", 
            features: "age, tenure, balance, num_products, is_active, estimated_salary",
            target_column: "churn",
            ml_task: "Classification",
            evaluation_metric: "ROC AUC",
            problem_statement: "Predicting whether a bank customer will churn within the next 6 months to implement retention strategies."
        })
      });
      if (!res.ok) throw new Error("Execution failed");
      const data = await res.json();
      setCategoryResults(data.results);
      setCategoryTime(data.execution_time);
    } catch (e) {
      console.error(e);
    } finally {
      setRunningAll(false);
    }
  };

  return (
    <div className="flex flex-col h-full gap-6 p-6 min-h-screen bg-black text-white selection:bg-cyan-500/30">
      <Link href="/dashboard" className="text-gray-400 hover:text-white flex items-center gap-2 mb-2 w-fit">
        <ArrowLeft className="w-4 h-4" /> Back to Dashboard
      </Link>
      
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight flex items-center gap-2">
            <span>📊</span> Data Science & Machine Learning
          </h1>
          <p className="text-gray-400 mt-2 max-w-2xl">
            A collection of AI agents specialized in data analysis, machine learning, feature engineering, model evaluation, statistics, and predictive analytics.
          </p>
        </div>
      </div>

      <div className="flex items-center justify-between bg-white/5 p-4 rounded-xl border border-white/10">
        <div>
          <h3 className="font-semibold text-lg">Run Entire Category</h3>
          <p className="text-sm text-gray-400">Execute all 10 Data Science agents concurrently.</p>
        </div>
        <Button 
          onClick={handleRunAll}
          disabled={runningAll}
          className="bg-cyan-600 hover:bg-cyan-500 text-white"
        >
          {runningAll ? <Loader2 className="w-4 h-4 animate-spin mr-2" /> : <Play className="w-4 h-4 mr-2" />}
          Run Category
        </Button>
      </div>

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

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        <AnimatePresence>
          {agents.map((agent) => (
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
                <div className="mt-auto p-6 pt-0 flex justify-between items-center">
                  <Badge variant="outline" className="text-cyan-400 border-cyan-400/20 bg-cyan-400/10">
                    {agent.category}
                  </Badge>
                  <Button variant="ghost" size="sm" className="h-8 hover:bg-white/10 text-white">
                    <Play className="w-4 h-4 mr-2" /> Run
                  </Button>
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
