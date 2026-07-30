from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class SQLtoPandasAgent(BaseAgent):
    name = "SQL to Pandas"
    description = "Converts SQL queries to Pandas syntax."
    category = "Data Science"
    icon = "Shuffle"
    system_prompt = """Convert the provided SQL query into equivalent Pandas syntax."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
