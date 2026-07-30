from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class HallucinationCheckerAgent(BaseAgent):
    name = "Hallucination Checker"
    description = "Identifies potential factual errors."
    category = "AI Utilities"
    icon = "Eye"
    system_prompt = """Review the text and highlight statements that might be AI hallucinations requiring verification."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
