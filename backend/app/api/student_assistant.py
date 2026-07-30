from fastapi import APIRouter, HTTPException, Body
from typing import Any
from app.registry.agent_registry import registry
from app.engine.execution import ExecutionEngine
from app.schemas.models import AgentOutput, CategoryExecutionResult

router = APIRouter()

@router.get("/agents/student-assistant")
async def get_student_agents():
    agents = registry.get_category("Student Assistant")
    return [
        {
            "name": a.name,
            "description": a.description,
            "category": a.category,
            "icon": a.icon
        } for a in agents
    ]

@router.post("/execute/student-assistant/run-all", response_model=CategoryExecutionResult)
async def run_all_student(input_data: Any = Body(...)):
    agents = registry.get_category("Student Assistant")
    if not agents:
        raise HTTPException(status_code=404, detail="No Student Assistant agents found.")
    
    return await ExecutionEngine.execute_category("Student Assistant", agents, input_data)

@router.post("/execute/student-assistant/{agent_name}", response_model=AgentOutput)
async def execute_student_agent(agent_name: str, input_data: Any = Body(...)):
    # Find the agent
    agent = registry.get_agent(agent_name)
    if not agent or agent.category != "Student Assistant":
        raise HTTPException(status_code=404, detail=f"Student Assistant Agent '{agent_name}' not found.")
    
    return await ExecutionEngine.execute_agent(agent, input_data)
