from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class IncidentResponsePlannerAgent(BaseAgent):
    name = "Incident Response Planner"
    description = "Drafts IR playbooks."
    category = "Cyber Security"
    icon = "Clipboard"
    system_prompt = """Create an incident response playbook for the specified security event."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
