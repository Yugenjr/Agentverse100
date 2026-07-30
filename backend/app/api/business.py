from fastapi import APIRouter, HTTPException, Body
from typing import Any
from app.registry.agent_registry import registry
from app.engine.execution import ExecutionEngine
from app.schemas.models import AgentOutput, CategoryExecutionResult

router = APIRouter()

@router.get("/agents/business")
async def get_business_agents():
    agents = registry.get_category("Business")
    return [
        {
            "name": a.name,
            "description": a.description,
            "category": a.category,
            "icon": a.icon
        } for a in agents
    ]

@router.post("/execute/business/run-all", response_model=CategoryExecutionResult)
async def run_all_business(input_data: Any = Body(...)):
    agents = registry.get_category("Business")
    if not agents:
        raise HTTPException(status_code=404, detail="No Business agents found.")
    
    return await ExecutionEngine.execute_category("Business", agents, input_data)

@router.post("/execute/business/{agent_name}", response_model=AgentOutput)
async def execute_business_agent(agent_name: str, input_data: Any = Body(...)):
    agent = registry.get_agent(agent_name)
    if not agent or agent.category != "Business":
        raise HTTPException(status_code=404, detail=f"Business Agent '{agent_name}' not found.")
    
    return await ExecutionEngine.execute_agent(agent, input_data)
