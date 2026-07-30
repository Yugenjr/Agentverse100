from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class GameIdeaGeneratorAgent(BaseAgent):
    name = "Game Idea Generator"
    description = "Brainstorms video game concepts."
    category = "Creative"
    icon = "Play"
    system_prompt = """Generate a unique concept for a video game including mechanics and story."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
