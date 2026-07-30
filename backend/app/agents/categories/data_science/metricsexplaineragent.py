from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class MetricsExplainerAgent(BaseAgent):
    name = "Metrics Explainer"
    description = "Explains ML evaluation metrics."
    category = "Data Science"
    icon = "Target"
    system_prompt = """Explain what the given ML evaluation metric means and when to use it."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
