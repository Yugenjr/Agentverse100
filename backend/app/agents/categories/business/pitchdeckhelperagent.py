from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PitchDeckHelperAgent(BaseAgent):
    name = "Pitch Deck Helper"
    description = "Suggests structure for pitch decks."
    category = "Business"
    icon = "Presentation"
    system_prompt = """Create a slide-by-slide outline for a pitch deck."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
