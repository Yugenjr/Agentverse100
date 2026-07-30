from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class RAGQueryOptimizerAgent(BaseAgent):
    name = "RAG Query Optimizer"
    description = "Optimizes search queries for RAG."
    category = "AI Utilities"
    icon = "Search"
    system_prompt = """Rewrite the user query to maximize retrieval success in a vector database."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
