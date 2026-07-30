from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class SQLOptimizerAgent(BaseAgent):
    name = "SQL Optimizer"
    description = "Optimizes SQL queries for performance."
    category = "Programming"
    icon = "Database"
    system_prompt = """Analyze and optimize the provided SQL query."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
