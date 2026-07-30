export interface Agent {
  name: string;
  description: string;
  category: string;
  icon: string;
}

export interface Category {
  name: string;
  count: number;
}

export interface AgentOutput {
  status: string;
  execution_time: number;
  agent_name: string;
  category: string;
  output: any;
  logs: string[];
}

export interface CategoryExecutionResult {
  category_name: string;
  execution_time: number;
  results: AgentOutput[];
}

export interface PipelineNode {
  agent_name: string;
}

export interface PipelineExecutionResult {
  status: string;
  total_execution_time: number;
  steps: AgentOutput[];
  final_output: any;
}
