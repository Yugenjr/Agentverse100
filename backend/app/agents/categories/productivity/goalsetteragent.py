from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class GoalSetterAgent(BaseAgent):
    name = "Goal Setter"
    description = "Helps set SMART goals."
    category = "Productivity"
    icon = "Target"
    system_prompt = """Convert the user's vague goal into a SMART goal."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
