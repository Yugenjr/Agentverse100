from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class JokeGeneratorAgent(BaseAgent):
    name = "Joke Generator"
    description = "Tells jokes on specific topics."
    category = "Creative"
    icon = "Smile"
    system_prompt = """Write a clever joke or pun about the requested topic."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
