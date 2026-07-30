from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class NegotiationCoachAgent(BaseAgent):
    name = "Negotiation Coach"
    description = "Provides tips for business negotiations."
    category = "Business"
    icon = "Handshake"
    system_prompt = """Provide strategic advice for negotiating the specified scenario."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
