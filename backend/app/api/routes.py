from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

from app.registry.agent_registry import registry
from app.engine.execution import ExecutionEngine
from app.schemas.models import (
    ExecuteAgentRequest, 
    ExecuteCategoryRequest, 
    ExecutePipelineRequest,
    AgentOutput,
    CategoryExecutionResult,
    PipelineExecutionResult
)

from app.api.text_processing import router as tp_router
from app.api.programming import router as prog_router

router = APIRouter()
router.include_router(tp_router)
router.include_router(prog_router)

@router.get("/agents")
async def get_agents(search: str = None):
    if search:
        agents = registry.search(search)
    else:
        agents = registry.get_all()
    
    return [
        {
            "name": a.name,
            "description": a.description,
            "category": a.category,
            "icon": a.icon
        } for a in agents
    ]

@router.get("/categories")
async def get_categories():
    categories = registry.get_all_categories()
    return [{"name": c, "count": len(registry.get_category(c))} for c in categories]

@router.post("/execute", response_model=AgentOutput)
async def execute_agent(req: ExecuteAgentRequest):
    agent = registry.get_agent(req.agent_name)
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agent '{req.agent_name}' not found.")
    
    return await ExecutionEngine.execute_agent(agent, req.input_data)

@router.post("/execute/category", response_model=CategoryExecutionResult)
async def execute_category(req: ExecuteCategoryRequest):
    agents = registry.get_category(req.category_name)
    if not agents:
        raise HTTPException(status_code=404, detail=f"Category '{req.category_name}' not found or empty.")
    
    return await ExecutionEngine.execute_category(req.category_name, agents, req.input_data)

@router.post("/pipeline", response_model=PipelineExecutionResult)
async def execute_pipeline(req: ExecutePipelineRequest):
    pipeline_agents = []
    for node in req.pipeline:
        agent = registry.get_agent(node.agent_name)
        if not agent:
            raise HTTPException(status_code=404, detail=f"Agent '{node.agent_name}' not found.")
        pipeline_agents.append(agent)
        
    return await ExecutionEngine.execute_pipeline(req.initial_input, pipeline_agents)
