from fastapi import APIRouter, HTTPException, Body
from typing import Any
from app.registry.agent_registry import registry
from app.engine.execution import ExecutionEngine
from app.schemas.models import AgentOutput, CategoryExecutionResult

router = APIRouter()

@router.get("/agents/datascience")
async def get_datascience_agents():
    agents = registry.get_category("Data Science")
    return [
        {
            "name": a.name,
            "description": a.description,
            "category": a.category,
            "icon": a.icon
        } for a in agents
    ]

@router.post("/execute/datascience/run-all", response_model=CategoryExecutionResult)
async def run_all_datascience(input_data: Any = Body(...)):
    agents = registry.get_category("Data Science")
    if not agents:
        raise HTTPException(status_code=404, detail="No Data Science agents found.")
    
    return await ExecutionEngine.execute_category("Data Science", agents, input_data)

@router.post("/execute/datascience/{agent_name}", response_model=AgentOutput)
async def execute_datascience_agent(agent_name: str, input_data: Any = Body(...)):
    agent = registry.get_agent(agent_name)
    if not agent or agent.category != "Data Science":
        raise HTTPException(status_code=404, detail=f"Data Science Agent '{agent_name}' not found.")
    
    return await ExecutionEngine.execute_agent(agent, input_data)
