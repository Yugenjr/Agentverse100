from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class DocstringWriterAgent(BaseAgent):
    name = "Docstring Writer"
    description = "Adds docstrings to functions/classes."
    category = "Programming"
    icon = "AlignLeft"
    system_prompt = """Write detailed docstrings for the provided Python code using Google style."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
