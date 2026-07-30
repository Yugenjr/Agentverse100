from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class DialogueWriterAgent(BaseAgent):
    name = "Dialogue Writer"
    description = "Writes engaging dialogue between characters."
    category = "Creative"
    icon = "MessageSquare"
    system_prompt = """Write a dialogue snippet between two characters in the given scenario."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
