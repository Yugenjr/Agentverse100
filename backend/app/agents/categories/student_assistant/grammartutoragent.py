from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class GrammarTutorAgent(BaseAgent):
    name = "Grammar Tutor"
    description = "Explains grammar rules with examples."
    category = "Student Assistant"
    icon = "Feather"
    system_prompt = """Explain the grammar rule in question and provide examples."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
