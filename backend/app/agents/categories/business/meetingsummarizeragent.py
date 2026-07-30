from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class MeetingSummarizerAgent(BaseAgent):
    name = "Meeting Summarizer"
    description = "Summarizes meeting transcripts."
    category = "Business"
    icon = "Users"
    system_prompt = """Extract action items and key decisions from the meeting transcript."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
