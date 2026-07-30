from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class WorldBuilderAgent(BaseAgent):
    name = "World Builder"
    description = "Fleshes out fictional worlds."
    category = "Creative"
    icon = "Globe"
    system_prompt = """Describe the geography, culture, and magic/tech system of a fictional world."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
