from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class StoryGeneratorAgent(BaseAgent):
    name = "Story Generator"
    description = "Generates creative short stories."
    category = "Creative"
    icon = "Book"
    system_prompt = """Write a creative and engaging short story based on the prompt."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
