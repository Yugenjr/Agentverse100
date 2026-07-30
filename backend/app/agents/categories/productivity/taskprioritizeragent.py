from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class TaskPrioritizerAgent(BaseAgent):
    name = "Task Prioritizer"
    description = "Organizes tasks using frameworks like Eisenhower."
    category = "Productivity"
    icon = "List"
    system_prompt = """Categorize the provided tasks using the Eisenhower Matrix."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
