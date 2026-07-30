from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class SecureCodingGuideAgent(BaseAgent):
    name = "Secure Coding Guide"
    description = "Provides secure coding practices."
    category = "Cyber Security"
    icon = "ShieldCheck"
    system_prompt = """Provide secure coding guidelines for the specified language."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
