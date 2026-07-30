from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class PhishingAnalyzerAgent(BaseAgent):
    name = "Phishing Analyzer"
    description = "Analyzes emails for phishing signs."
    category = "Cyber Security"
    icon = "AlertTriangle"
    system_prompt = """Analyze the provided email text and highlight potential phishing indicators."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
