from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class NameGeneratorAgent(BaseAgent):
    name = "Name Generator"
    description = "Generates fantasy or sci-fi names."
    category = "Creative"
    icon = "Tag"
    system_prompt = """Generate 10 unique names suitable for the requested setting."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
