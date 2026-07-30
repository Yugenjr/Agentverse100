from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class CharacterCreatorAgent(BaseAgent):
    name = "Character Creator"
    description = "Builds detailed fictional characters."
    category = "Creative"
    icon = "User"
    system_prompt = """Create a detailed character profile including backstory, motivations, and flaws."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
