from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class LogAnalyzerAgent(BaseAgent):
    name = "Log Analyzer"
    description = "Finds anomalies in log excerpts."
    category = "Cyber Security"
    icon = "Terminal"
    system_prompt = """Analyze the log snippet and identify any suspicious activity."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
