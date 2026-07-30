from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class MarketResearcherAgent(BaseAgent):
    name = "Market Researcher"
    description = "Provides high-level market trends."
    category = "Business"
    icon = "TrendingUp"
    system_prompt = """Summarize current market trends for the specified industry."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
