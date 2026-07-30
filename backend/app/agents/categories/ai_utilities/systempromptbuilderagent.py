from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class SystemPromptBuilderAgent(BaseAgent):
    name = "System Prompt Builder"
    description = "Generates system prompts for new agents."
    category = "AI Utilities"
    icon = "Cpu"
    system_prompt = """Draft a comprehensive system prompt for the described AI persona."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
