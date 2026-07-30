from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class ModelSelectorAgent(BaseAgent):
    name = "Model Selector"
    description = "Recommends machine learning models."
    category = "Data Science"
    icon = "Box"
    system_prompt = """Recommend the best machine learning algorithms for this specific problem."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
