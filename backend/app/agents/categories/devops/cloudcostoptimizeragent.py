from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class CloudCostOptimizerAgent(BaseAgent):
    name = "Cloud Cost Optimizer"
    description = "Suggests ways to reduce cloud bills."
    category = "DevOps"
    icon = "DollarSign"
    system_prompt = """Suggest architectural changes to reduce costs for the described cloud setup."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
