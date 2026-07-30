from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PoemWriterAgent(BaseAgent):
    name = "Poem Writer"
    description = "Writes poems in various styles."
    category = "Creative"
    icon = "Feather"
    system_prompt = """Write a poem in the requested style about the given topic."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
