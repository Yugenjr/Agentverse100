import time
import asyncio
from typing import Any, List
from rich.console import Console

from app.schemas.models import AgentOutput, CategoryExecutionResult, PipelineExecutionResult, PipelineNode

console = Console()

class ExecutionEngine:
    @staticmethod
    async def execute_agent(agent, input_data: Any) -> AgentOutput:
        start_time = time.time()
        console.print(f"[bold cyan]Started[/bold cyan] {agent.name}")
        console.print(f"[bold yellow]Thinking & Calling LLM...[/bold yellow]")
        
        try:
            # We call the agent's execute which uses groq_service
            output = await agent.execute(input_data)
            status = "success"
        except Exception as e:
            output = str(e)
            status = "failed"
            
        execution_time = round(time.time() - start_time, 2)
        console.print(f"[bold green]Completed[/bold green] {agent.name} in {execution_time}s")
        
        return AgentOutput(
            status=status,
            execution_time=execution_time,
            agent_name=agent.name,
            category=agent.category,
            output=output,
            logs=[f"Started {agent.name}", f"Thinking...", f"Completed in {execution_time}s"]
        )

    @staticmethod
    async def execute_category(category_name: str, agents: List[Any], input_data: Any) -> CategoryExecutionResult:
        start_time = time.time()
        
        # Concurrently execute all agents in the category
        tasks = [ExecutionEngine.execute_agent(agent, input_data) for agent in agents]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter out exception objects if any (though execute_agent handles them)
        valid_results = [r for r in results if isinstance(r, AgentOutput)]
        
        total_time = round(time.time() - start_time, 2)
        return CategoryExecutionResult(
            category_name=category_name,
            execution_time=total_time,
            results=valid_results
        )

    @staticmethod
    async def execute_pipeline(initial_input: Any, pipeline: List[Any]) -> PipelineExecutionResult:
        start_time = time.time()
        current_input = initial_input
        steps = []
        
        for agent in pipeline:
            result = await ExecutionEngine.execute_agent(agent, current_input)
            steps.append(result)
            if result.status == "failed":
                return PipelineExecutionResult(
                    status="failed_at_step",
                    total_execution_time=round(time.time() - start_time, 2),
                    steps=steps,
                    final_output=current_input
                )
            # The output of the previous step becomes the input to the next
            current_input = result.output
            
        total_time = round(time.time() - start_time, 2)
        return PipelineExecutionResult(
            status="success",
            total_execution_time=total_time,
            steps=steps,
            final_output=current_input
        )
