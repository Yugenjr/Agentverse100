from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class K8sManifestWriterAgent(BaseAgent):
    name = "K8s Manifest Writer"
    description = "Generates Kubernetes YAMLs."
    category = "DevOps"
    icon = "Layers"
    system_prompt = """Write the required Kubernetes manifests (Deployment, Service, etc.) for the app."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
