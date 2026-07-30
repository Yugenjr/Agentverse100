from typing import Dict, Optional
from groq import AsyncGroq
from app.core.config import settings

class GroqManager:
    def __init__(self):
        self.clients: Dict[str, Optional[AsyncGroq]] = {}
        self.model = settings.LLM_MODEL
        
        # Initialize 10 Groq clients mapped to categories
        self.clients["Text Processing"] = AsyncGroq(api_key=settings.GROQ_API_KEY_1) if settings.GROQ_API_KEY_1 else None
        self.clients["Programming"] = AsyncGroq(api_key=settings.GROQ_API_KEY_2) if settings.GROQ_API_KEY_2 else None
        self.clients["Student Assistant"] = AsyncGroq(api_key=settings.GROQ_API_KEY_3) if settings.GROQ_API_KEY_3 else None
        self.clients["Business"] = AsyncGroq(api_key=settings.GROQ_API_KEY_4) if settings.GROQ_API_KEY_4 else None
        self.clients["Data Science"] = AsyncGroq(api_key=settings.GROQ_API_KEY_5) if settings.GROQ_API_KEY_5 else None
        self.clients["Cyber Security"] = AsyncGroq(api_key=settings.GROQ_API_KEY_6) if settings.GROQ_API_KEY_6 else None
        self.clients["Productivity"] = AsyncGroq(api_key=settings.GROQ_API_KEY_7) if settings.GROQ_API_KEY_7 else None
        self.clients["Creative"] = AsyncGroq(api_key=settings.GROQ_API_KEY_8) if settings.GROQ_API_KEY_8 else None
        self.clients["DevOps"] = AsyncGroq(api_key=settings.GROQ_API_KEY_9) if settings.GROQ_API_KEY_9 else None
        self.clients["AI Utilities"] = AsyncGroq(api_key=settings.GROQ_API_KEY_10) if settings.GROQ_API_KEY_10 else None

    def get_client(self, category: str) -> Optional[AsyncGroq]:
        return self.clients.get(category)

    async def generate_response(self, category: str, system_prompt: str, user_prompt: str) -> str:
        client = self.get_client(category)
        if not client:
            return f"Error: No Groq API client configured for category '{category}'"
        
        try:
            response = await client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                model=self.model,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling Groq API: {str(e)}"

groq_manager = GroqManager()
