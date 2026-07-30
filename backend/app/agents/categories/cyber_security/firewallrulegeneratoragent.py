from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class FirewallRuleGeneratorAgent(BaseAgent):
    name = "Firewall Rule Generator"
    description = "Helps write iptables/firewall rules."
    category = "Cyber Security"
    icon = "Server"
    system_prompt = """Provide the exact firewall rules to achieve the requested network policy."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
