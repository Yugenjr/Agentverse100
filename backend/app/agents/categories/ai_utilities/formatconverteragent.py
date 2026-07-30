from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class FormatConverterAgent(BaseAgent):
    name = "Format Converter"
    description = "Converts between JSON/XML/YAML/CSV."
    category = "AI Utilities"
    icon = "File"
    system_prompt = """Convert the provided data structure into the requested format (e.g., JSON to YAML)."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
