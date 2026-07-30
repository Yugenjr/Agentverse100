from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class MonitoringAlertConfigAgent(BaseAgent):
    name = "Monitoring Alert Config"
    description = "Drafts Prometheus alert rules."
    category = "DevOps"
    icon = "Bell"
    system_prompt = """Write Prometheus alerting rules for the specified metrics."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
