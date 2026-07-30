from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class CICDPlannerAgent(BaseAgent):
    name = "CI/CD Planner"
    description = "Designs CI/CD pipelines."
    category = "DevOps"
    icon = "GitMerge"
    system_prompt = """Design a CI/CD pipeline workflow for the given project."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
