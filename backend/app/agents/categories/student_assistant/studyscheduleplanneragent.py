from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class StudySchedulePlannerAgent(BaseAgent):
    name = "Study Schedule Planner"
    description = "Creates realistic study schedules."
    category = "Student Assistant"
    icon = "Calendar"
    system_prompt = """Create a structured study schedule based on the topics and time available."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
