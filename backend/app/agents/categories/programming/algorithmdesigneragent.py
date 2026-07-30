from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class AlgorithmDesignerAgent(BaseAgent):
    name = "Algorithm Designer"
    description = "Designs algorithms for specific problems."
    category = "Programming"
    icon = "Cpu"
    system_prompt = """Provide an algorithmic solution (with pseudocode) for the given problem."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
