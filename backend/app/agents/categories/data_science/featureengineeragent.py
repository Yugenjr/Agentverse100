from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class FeatureEngineerAgent(BaseAgent):
    name = "Feature Engineer"
    description = "Suggests new features from existing data."
    category = "Data Science"
    icon = "Zap"
    system_prompt = """Suggest new features that could be engineered from the provided dataset."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
