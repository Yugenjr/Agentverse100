from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class MorningRoutineAgent(BaseAgent):
    name = "Morning Routine"
    description = "Suggests optimal morning routines."
    category = "Productivity"
    icon = "Sunrise"
    system_prompt = """Design a morning routine based on the user's preferences."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
