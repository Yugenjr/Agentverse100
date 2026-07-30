from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class DebatePrepAgent(BaseAgent):
    name = "Debate Prep"
    description = "Provides arguments for both sides of a topic."
    category = "Student Assistant"
    icon = "MessageCircle"
    system_prompt = """Provide strong arguments for and against the given topic."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
