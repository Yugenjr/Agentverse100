from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class EmbeddingsExplainerAgent(BaseAgent):
    name = "Embeddings Explainer"
    description = "Explains vector embeddings simply."
    category = "AI Utilities"
    icon = "Compass"
    system_prompt = """Explain how vector embeddings work and how they relate to the prompt."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
