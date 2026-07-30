from abc import ABC, abstractmethod
from typing import Any
from app.schemas.models import AgentOutput
from app.services.groq_manager import groq_manager

class BaseAgent(ABC):
    name: str = "Base Agent"
    description: str = "Base description"
    category: str = "Uncategorized"
    icon: str = "Bot"
    system_prompt: str = "You are a helpful assistant."

    def __init__(self):
        # The agent automatically receives the Groq client assigned to its category
        self.groq_client = groq_manager.get_client(self.category)

    async def generate_response(self, user_prompt: str) -> str:
        return await groq_manager.generate_response(self.category, self.system_prompt, user_prompt)

    @abstractmethod
    async def execute(self, input_data: Any) -> AgentOutput:
        """
        Execute the agent logic.
        This must be implemented by all subclasses.
        """
        pass
