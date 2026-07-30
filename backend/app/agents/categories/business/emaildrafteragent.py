from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class EmailDrafterAgent(BaseAgent):
    name = "Email Drafter"
    description = "Drafts professional business emails."
    category = "Business"
    icon = "Mail"
    system_prompt = """Draft a professional business email based on the prompt."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
