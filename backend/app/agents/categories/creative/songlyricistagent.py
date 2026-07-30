from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput

class SongLyricistAgent(BaseAgent):
    name = "Song Lyricist"
    description = "Writes lyrics for songs."
    category = "Creative"
    icon = "Music"
    system_prompt = """Write a verse and chorus for a song based on the theme."""

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {input_data}"
        response = await self.generate_response(user_prompt)
        return response
