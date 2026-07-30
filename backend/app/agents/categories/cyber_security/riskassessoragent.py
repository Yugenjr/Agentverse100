from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class RiskAssessorAgent(BaseAgent):
    name = "Risk Assessor"
    description = "Calculates security risks based on impact."
    category = "Cyber Security"
    icon = "AlertOctagon"
    system_prompt = """Perform a qualitative risk assessment for the described scenario."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
