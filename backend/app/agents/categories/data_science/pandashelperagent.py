from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PandasHelperAgent(BaseAgent):
    name = "Pandas Helper"
    description = "Generates pandas code for data manipulation."
    category = "Data Science"
    icon = "Table"
    system_prompt = """Provide pandas code to achieve the data manipulation described."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
