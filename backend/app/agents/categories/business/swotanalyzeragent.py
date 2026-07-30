from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class SWOTAnalyzerAgent(BaseAgent):
    name = "SWOT Analyzer"
    description = "Performs SWOT analysis on a business idea."
    category = "Business"
    icon = "Crosshair"
    system_prompt = """Conduct a Strengths, Weaknesses, Opportunities, and Threats analysis."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
