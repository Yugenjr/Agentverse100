from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PerformanceReviewerAgent(BaseAgent):
    name = "Performance Reviewer"
    description = "Helps draft performance reviews."
    category = "Business"
    icon = "Star"
    system_prompt = """Draft a constructive and professional performance review."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
