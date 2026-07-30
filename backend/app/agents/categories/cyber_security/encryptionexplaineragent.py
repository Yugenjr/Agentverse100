from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class EncryptionExplainerAgent(BaseAgent):
    name = "Encryption Explainer"
    description = "Explains cryptographic algorithms."
    category = "Cyber Security"
    icon = "Key"
    system_prompt = """Explain how the specified encryption algorithm works in simple terms."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
