import { Agent, Category, AgentOutput, CategoryExecutionResult, PipelineExecutionResult, PipelineNode } from '../types';

const API_BASE = 'http://localhost:8000/api';

export async function fetchAgents(search?: string): Promise<Agent[]> {
  const url = search ? `${API_BASE}/agents?search=${encodeURIComponent(search)}` : `${API_BASE}/agents`;
  const res = await fetch(url);
  if (!res.ok) throw new Error("Failed to fetch agents");
  return res.json();
}

export async function fetchCategories(): Promise<Category[]> {
  const res = await fetch(`${API_BASE}/categories`);
  if (!res.ok) throw new Error("Failed to fetch categories");
  return res.json();
}

export async function executeAgent(agentName: string, inputData: any): Promise<AgentOutput> {
  const res = await fetch(`${API_BASE}/execute`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ agent_name: agentName, input_data: inputData })
  });
  if (!res.ok) throw new Error("Failed to execute agent");
  return res.json();
}

export async function executeCategory(categoryName: string, inputData: any): Promise<CategoryExecutionResult> {
  const res = await fetch(`${API_BASE}/execute/category`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ category_name: categoryName, input_data: inputData })
  });
  if (!res.ok) throw new Error("Failed to execute category");
  return res.json();
}

export async function executePipeline(initialInput: any, pipeline: PipelineNode[]): Promise<PipelineExecutionResult> {
  const res = await fetch(`${API_BASE}/pipeline`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ initial_input: initialInput, pipeline })
  });
  if (!res.ok) throw new Error("Failed to execute pipeline");
  return res.json();
}
