from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class BugFinderAgent(BaseAgent):
    name = "Bug Finder"
    description = "Identifies potential bugs in code."
    category = "Programming"
    icon = "Bug"
    system_prompt = """Analyze the code and identify any potential bugs or edge cases."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
