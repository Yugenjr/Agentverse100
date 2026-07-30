from fastapi import APIRouter, HTTPException, Body
from typing import Any
from app.registry.agent_registry import registry
from app.engine.execution import ExecutionEngine
from app.schemas.models import AgentOutput, CategoryExecutionResult

router = APIRouter()

@router.get("/agents/programming")
async def get_programming_agents():
    agents = registry.get_category("Programming")
    return [
        {
            "name": a.name,
            "description": a.description,
            "category": a.category,
            "icon": a.icon
        } for a in agents
    ]

@router.post("/execute/programming/run-all", response_model=CategoryExecutionResult)
async def run_all_programming(input_data: Any = Body(...)):
    agents = registry.get_category("Programming")
    if not agents:
        raise HTTPException(status_code=404, detail="No Programming agents found.")
    
    return await ExecutionEngine.execute_category("Programming", agents, input_data)

@router.post("/execute/programming/{agent_name}", response_model=AgentOutput)
async def execute_programming_agent(agent_name: str, input_data: Any = Body(...)):
    # Find the agent
    agent = registry.get_agent(agent_name)
    if not agent or agent.category != "Programming":
        raise HTTPException(status_code=404, detail=f"Programming Agent '{agent_name}' not found.")
    
    return await ExecutionEngine.execute_agent(agent, input_data)
