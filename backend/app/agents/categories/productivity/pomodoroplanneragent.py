from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PomodoroPlannerAgent(BaseAgent):
    name = "Pomodoro Planner"
    description = "Creates custom Pomodoro schedules."
    category = "Productivity"
    icon = "Clock"
    system_prompt = """Create a detailed Pomodoro schedule based on the user's tasks and time."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
