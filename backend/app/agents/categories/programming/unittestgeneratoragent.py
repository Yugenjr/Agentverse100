from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class UnitTestGeneratorAgent(BaseAgent):
    name = "Unit Test Generator"
    description = "Generates unit tests for functions."
    category = "Programming"
    icon = "TestTube"
    system_prompt = """Write comprehensive unit tests for the provided code."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
