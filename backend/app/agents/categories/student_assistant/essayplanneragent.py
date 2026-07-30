from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class EssayPlannerAgent(BaseAgent):
    name = "Essay Planner"
    description = "Creates outlines for essays."
    category = "Student Assistant"
    icon = "Edit3"
    system_prompt = """Provide a structured outline for an essay based on the topic."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
