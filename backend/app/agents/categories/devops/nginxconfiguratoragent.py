from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class NginxConfiguratorAgent(BaseAgent):
    name = "Nginx Configurator"
    description = "Writes Nginx server blocks."
    category = "DevOps"
    icon = "Server"
    system_prompt = """Write an Nginx configuration file for the specified routing requirements."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
