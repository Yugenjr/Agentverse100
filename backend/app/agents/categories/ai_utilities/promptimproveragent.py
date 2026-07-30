from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PromptImproverAgent(BaseAgent):
    name = "Prompt Improver"
    description = "Refines prompts for better LLM outputs."
    category = "AI Utilities"
    icon = "Edit"
    system_prompt = """Rewrite the user's prompt to be more detailed, clear, and effective for an LLM."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
