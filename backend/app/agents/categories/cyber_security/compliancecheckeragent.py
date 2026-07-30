from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class ComplianceCheckerAgent(BaseAgent):
    name = "Compliance Checker"
    description = "Checks requirements for SOC2/GDPR."
    category = "Cyber Security"
    icon = "CheckCircle"
    system_prompt = """Explain the requirements for the specified compliance framework."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
