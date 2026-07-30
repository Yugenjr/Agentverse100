from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class TokenEstimatorAgent(BaseAgent):
    name = "Token Estimator"
    description = "Estimates token counts (conceptual)."
    category = "AI Utilities"
    icon = "Hash"
    system_prompt = """Estimate the relative token size of the text and explain tokenization concepts."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
