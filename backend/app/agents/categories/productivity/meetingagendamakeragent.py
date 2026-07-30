from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class MeetingAgendaMakerAgent(BaseAgent):
    name = "Meeting Agenda Maker"
    description = "Drafts clear agendas for meetings."
    category = "Productivity"
    icon = "FileText"
    system_prompt = """Create a structured meeting agenda based on the topics."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
