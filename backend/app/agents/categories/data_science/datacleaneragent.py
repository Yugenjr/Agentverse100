from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class DataCleanerAgent(BaseAgent):
    name = "Data Cleaner"
    description = "Suggests steps to clean dirty datasets."
    category = "Data Science"
    icon = "Trash2"
    system_prompt = """Outline the steps required to clean and preprocess the described dataset."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
