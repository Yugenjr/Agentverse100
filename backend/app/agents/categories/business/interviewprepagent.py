from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class InterviewPrepAgent(BaseAgent):
    name = "Interview Prep"
    description = "Generates interview questions."
    category = "Business"
    icon = "Mic"
    system_prompt = """Generate 5 behavioral and 5 technical interview questions for the role."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
