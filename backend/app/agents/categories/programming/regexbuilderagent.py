from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class RegexBuilderAgent(BaseAgent):
    name = "Regex Builder"
    description = "Creates regular expressions from descriptions."
    category = "Programming"
    icon = "Hash"
    system_prompt = """Provide a regex pattern that matches the user's description."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
