from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class InboxZeroHelperAgent(BaseAgent):
    name = "Inbox Zero Helper"
    description = "Categorizes unorganized email text."
    category = "Productivity"
    icon = "Mail"
    system_prompt = """Suggest folders or actions (Reply, Delegate, Delete) for the email summaries."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
