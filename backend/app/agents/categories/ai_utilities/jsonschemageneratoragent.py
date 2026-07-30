from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class JSONSchemaGeneratorAgent(BaseAgent):
    name = "JSON Schema Generator"
    description = "Generates JSON schemas from examples."
    category = "AI Utilities"
    icon = "Code"
    system_prompt = """Create a valid JSON schema that matches the provided JSON data."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
