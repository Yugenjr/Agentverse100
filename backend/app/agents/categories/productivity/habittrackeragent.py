from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class HabitTrackerAgent(BaseAgent):
    name = "Habit Tracker"
    description = "Suggests habit loops and routines."
    category = "Productivity"
    icon = "CheckSquare"
    system_prompt = """Design a daily routine and habit loop for the specified goal."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
