from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class TimeAuditorAgent(BaseAgent):
    name = "Time Auditor"
    description = "Analyzes how time was spent."
    category = "Productivity"
    icon = "PieChart"
    system_prompt = """Analyze the time log and provide insights on productivity leaks."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
