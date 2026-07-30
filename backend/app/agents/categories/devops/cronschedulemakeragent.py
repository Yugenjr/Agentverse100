from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class CronScheduleMakerAgent(BaseAgent):
    name = "Cron Schedule Maker"
    description = "Explains and generates cron expressions."
    category = "DevOps"
    icon = "Clock"
    system_prompt = """Provide the cron expression for the requested schedule and explain it."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
