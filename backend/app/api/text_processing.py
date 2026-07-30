from fastapi import APIRouter, HTTPException, Body
from typing import Any
from app.registry.agent_registry import registry
from app.engine.execution import ExecutionEngine
from app.schemas.models import AgentOutput, CategoryExecutionResult

router = APIRouter()

@router.get("/agents/text-processing")
async def get_text_processing_agents():
    agents = registry.get_category("Text Processing")
    return [
        {
            "name": a.name,
            "description": a.description,
            "category": a.category,
            "icon": a.icon
        } for a in agents
    ]

@router.post("/execute/text-processing/run-all", response_model=CategoryExecutionResult)
async def run_all_text_processing(input_data: Any = Body(...)):
    agents = registry.get_category("Text Processing")
    if not agents:
        raise HTTPException(status_code=404, detail="No Text Processing agents found.")
    
    return await ExecutionEngine.execute_category("Text Processing", agents, input_data)

@router.post("/execute/text-processing/{agent_name}", response_model=AgentOutput)
async def execute_text_processing_agent(agent_name: str, input_data: Any = Body(...)):
    # Find the agent
    # We might need to unquote or handle spaces in agent names if passed in URL
    agent = registry.get_agent(agent_name)
    if not agent or agent.category != "Text Processing":
        raise HTTPException(status_code=404, detail=f"Text Processing Agent '{agent_name}' not found.")
    
    return await ExecutionEngine.execute_agent(agent, input_data)
