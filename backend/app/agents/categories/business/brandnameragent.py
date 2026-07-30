from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class BrandNamerAgent(BaseAgent):
    name = "Brand Namer"
    description = "Brainstorms brand names and taglines."
    category = "Business"
    icon = "Tag"
    system_prompt = """Generate 10 catchy brand names and taglines for the business idea."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
