from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class TerraformBuilderAgent(BaseAgent):
    name = "Terraform Builder"
    description = "Creates Terraform scripts."
    category = "DevOps"
    icon = "Cloud"
    system_prompt = """Write Terraform code to provision the requested cloud infrastructure."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
