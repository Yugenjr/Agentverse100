from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PersonaAdopterAgent(BaseAgent):
    name = "Persona Adopter"
    description = "Adopts any persona requested."
    category = "AI Utilities"
    icon = "UserCheck"
    system_prompt = """Adopt the requested persona and respond entirely in character."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
