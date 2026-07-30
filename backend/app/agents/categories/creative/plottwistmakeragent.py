from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PlotTwistMakerAgent(BaseAgent):
    name = "Plot Twist Maker"
    description = "Suggests surprising plot twists."
    category = "Creative"
    icon = "Shuffle"
    system_prompt = """Suggest 3 surprising but logical plot twists for the story summary."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
