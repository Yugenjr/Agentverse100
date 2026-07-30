from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class CodeConverterAgent(BaseAgent):
    name = "Code Converter"
    description = "Translates code from one language to another."
    category = "Programming"
    icon = "Repeat"
    system_prompt = """Translate the provided code to the language requested."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
