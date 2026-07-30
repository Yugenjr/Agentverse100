from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class FewShotGeneratorAgent(BaseAgent):
    name = "Few-Shot Generator"
    description = "Creates few-shot examples for prompts."
    category = "AI Utilities"
    icon = "List"
    system_prompt = """Generate 3 diverse input/output examples for the specified task."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
