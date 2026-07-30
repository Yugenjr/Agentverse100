from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class ScienceExplainerAgent(BaseAgent):
    name = "Science Explainer"
    description = "Explains scientific concepts simply."
    category = "Student Assistant"
    icon = "Activity"
    system_prompt = """Explain the scientific concept as if to a high school student."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
