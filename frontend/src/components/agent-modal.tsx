import { useState } from "react";
import { Agent, AgentOutput, executeAgent } from "@/lib/api";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Loader2, Play } from "lucide-react";
import { Badge } from "@/components/ui/badge";

export function AgentModal({ agent, onClose }: { agent: Agent, onClose: () => void }) {
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AgentOutput | null>(null);

  const handleRun = async () => {
    if (!input) return;
    setLoading(true);
    try {
      const res = await executeAgent(agent.name, input);
      setResult(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Dialog open={true} onOpenChange={(open) => !open && onClose()}>
      <DialogContent className="sm:max-w-[700px] bg-zinc-950 border-white/10 text-white">
        <DialogHeader>
          <div className="flex items-center justify-between pr-6">
            <DialogTitle className="text-2xl">{agent.name}</DialogTitle>
            <Badge variant="outline" className="text-cyan-400 border-cyan-400/20 bg-cyan-400/10">
              {agent.category}
            </Badge>
          </div>
          <DialogDescription className="text-gray-400">
            {agent.description}
          </DialogDescription>
        </DialogHeader>

        <div className="grid gap-4 py-4">
          <div className="flex flex-col gap-2">
            <label className="text-sm font-medium text-gray-300">Input Data</label>
            <Textarea 
              placeholder={`Provide input for ${agent.name}...`}
              className="bg-white/5 border-white/10 text-white min-h-[100px]"
              value={input}
              onChange={(e) => setInput(e.target.value)}
            />
          </div>
          
          <Button 
            onClick={handleRun} 
            disabled={loading || !input}
            className="w-full bg-cyan-600 hover:bg-cyan-500"
          >
            {loading ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Play className="w-4 h-4 mr-2" />}
            Execute Agent
          </Button>

          {result && (
            <div className="mt-4 flex flex-col gap-2">
              <div className="flex items-center justify-between">
                <label className="text-sm font-medium text-gray-300">Execution Result</label>
                <span className="text-xs text-green-400 font-mono">Time: {result.execution_time}s</span>
              </div>
              <div className="p-4 bg-black/50 border border-white/10 rounded-lg text-sm text-gray-200 whitespace-pre-wrap font-mono min-h-[100px] max-h-[300px] overflow-y-auto">
                {result.output}
              </div>
              <div className="mt-2 text-xs text-gray-500 space-y-1">
                <p className="font-semibold text-gray-400">Logs:</p>
                {result.logs.map((log, i) => (
                  <div key={i}>&gt; {log}</div>
                ))}
              </div>
            </div>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}
