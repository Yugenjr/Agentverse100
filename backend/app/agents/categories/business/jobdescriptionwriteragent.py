from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class JobDescriptionWriterAgent(BaseAgent):
    name = "Job Description Writer"
    description = "Writes professional job postings."
    category = "Business"
    icon = "Briefcase"
    system_prompt = """Write a compelling job description based on the title and requirements."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
