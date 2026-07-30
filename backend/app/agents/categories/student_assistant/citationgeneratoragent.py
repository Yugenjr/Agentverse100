from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class CitationGeneratorAgent(BaseAgent):
    name = "Citation Generator"
    description = "Generates academic citations."
    category = "Student Assistant"
    icon = "Bookmark"
    system_prompt = """Format the provided source into APA and MLA citations."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
