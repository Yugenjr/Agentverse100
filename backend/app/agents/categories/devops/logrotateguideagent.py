from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class LogRotateGuideAgent(BaseAgent):
    name = "Log Rotate Guide"
    description = "Explains how to set up log rotation."
    category = "DevOps"
    icon = "RotateCcw"
    system_prompt = """Explain how to configure logrotate for the specified log files."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
