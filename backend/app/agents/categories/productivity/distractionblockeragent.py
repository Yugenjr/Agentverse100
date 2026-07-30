from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class DistractionBlockerAgent(BaseAgent):
    name = "Distraction Blocker"
    description = "Provides tips to avoid specific distractions."
    category = "Productivity"
    icon = "XOctagon"
    system_prompt = """Provide actionable advice to overcome the specific distraction."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
