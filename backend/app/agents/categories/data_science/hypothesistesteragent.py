from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class HypothesisTesterAgent(BaseAgent):
    name = "Hypothesis Tester"
    description = "Helps design statistical tests."
    category = "Data Science"
    icon = "HelpCircle"
    system_prompt = """Design a hypothesis test (Null, Alternative, test statistic) for the scenario."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
