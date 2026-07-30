from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class DockerfileGeneratorAgent(BaseAgent):
    name = "Dockerfile Generator"
    description = "Writes Dockerfiles for applications."
    category = "DevOps"
    icon = "Box"
    system_prompt = """Write an optimized Dockerfile for the specified application stack."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
