from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class DelegationMatrixAgent(BaseAgent):
    name = "Delegation Matrix"
    description = "Helps decide what to delegate."
    category = "Productivity"
    icon = "Users"
    system_prompt = """Analyze the tasks and identify which ones should be delegated."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
