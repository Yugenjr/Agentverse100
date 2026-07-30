from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime

class AgentOutput(BaseModel):
    status: str
    execution_time: float
    agent_name: str
    category: str
    output: Any
    logs: List[str]

class ExecuteAgentRequest(BaseModel):
    agent_name: str
    input_data: Any

class ExecuteCategoryRequest(BaseModel):
    category_name: str
    input_data: Any

class CategoryExecutionResult(BaseModel):
    category_name: str
    execution_time: float
    results: List[AgentOutput]

class PipelineNode(BaseModel):
    agent_name: str

class ExecutePipelineRequest(BaseModel):
    initial_input: Any
    pipeline: List[PipelineNode]

class PipelineExecutionResult(BaseModel):
    status: str
    total_execution_time: float
    steps: List[AgentOutput]
    final_output: Any
