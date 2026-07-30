from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class BashScriptWriterAgent(BaseAgent):
    name = "Bash Script Writer"
    description = "Writes shell scripts for automation."
    category = "DevOps"
    icon = "Terminal"
    system_prompt = """Write a robust bash script to automate the requested task."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
