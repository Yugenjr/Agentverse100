from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class MathSolverAgent(BaseAgent):
    name = "Math Solver"
    description = "Solves math problems with step-by-step reasoning."
    category = "Student Assistant"
    icon = "Calculator"
    system_prompt = """Solve the math problem step by step."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
