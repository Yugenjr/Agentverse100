from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class FlashcardCreatorAgent(BaseAgent):
    name = "Flashcard Creator"
    description = "Generates flashcards from study notes."
    category = "Student Assistant"
    icon = "Layers"
    system_prompt = """Create question/answer flashcards based on the notes."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
