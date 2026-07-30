from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class CodeRefactorerAgent(BaseAgent):
    name = "Code Refactorer"
    description = "Improves code quality and structure."
    category = "Programming"
    icon = "Wrench"
    system_prompt = """Refactor the provided code to follow best practices and improve readability."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
