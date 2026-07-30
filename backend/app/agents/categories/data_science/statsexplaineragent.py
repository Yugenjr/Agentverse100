from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class StatsExplainerAgent(BaseAgent):
    name = "Stats Explainer"
    description = "Explains statistical concepts clearly."
    category = "Data Science"
    icon = "PieChart"
    system_prompt = """Explain the statistical concept in an easy-to-understand way."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
