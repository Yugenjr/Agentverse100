from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class CodeExplainerAgent(BaseAgent):
    name = "Code Explainer"
    description = "Explains complex code snippets."
    category = "Programming"
    icon = "Code"
    system_prompt = """Explain the following code step by step."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
