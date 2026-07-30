from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class RegexforDataAgent(BaseAgent):
    name = "Regex for Data"
    description = "Writes regex to extract data from text."
    category = "Data Science"
    icon = "Filter"
    system_prompt = """Provide the exact regex pattern to extract the requested data."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
