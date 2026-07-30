from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PasswordPolicyMakerAgent(BaseAgent):
    name = "Password Policy Maker"
    description = "Generates strong password policies."
    category = "Cyber Security"
    icon = "Lock"
    system_prompt = """Draft a comprehensive password policy for an organization."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
