from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class VocabularyBuilderAgent(BaseAgent):
    name = "Vocabulary Builder"
    description = "Suggests synonyms and word usages."
    category = "Student Assistant"
    icon = "Type"
    system_prompt = """Provide synonyms, antonyms, and example sentences for the word."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
