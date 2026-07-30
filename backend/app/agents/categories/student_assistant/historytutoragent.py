from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class HistoryTutorAgent(BaseAgent):
    name = "History Tutor"
    description = "Answers historical questions."
    category = "Student Assistant"
    icon = "Clock"
    system_prompt = """You are an expert history tutor. Answer the questions accurately."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
