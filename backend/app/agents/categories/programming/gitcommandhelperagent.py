from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class GitCommandHelperAgent(BaseAgent):
    name = "Git Command Helper"
    description = "Suggests git commands for workflows."
    category = "Programming"
    icon = "GitCommit"
    system_prompt = """Provide the correct git commands to achieve the user's workflow."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
