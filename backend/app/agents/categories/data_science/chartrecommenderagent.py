from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class ChartRecommenderAgent(BaseAgent):
    name = "Chart Recommender"
    description = "Suggests the best visualization for data."
    category = "Data Science"
    icon = "BarChart2"
    system_prompt = """Recommend the best chart types for visualizing this data and explain why."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
