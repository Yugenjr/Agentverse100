from typing import Any
import os
import time
from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput
from app.schemas.text_processing_schemas import ToneChangerInput

class ToneChangerAgent(BaseAgent):
    name = "Tone Changer"
    description = "Rewrite text to match Formal, Casual, Professional, Friendly, or Academic tones."
    category = "Text Processing"
    icon = "MessageSquare"
    
    def _load_prompt(self) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'prompts', 'text_processing', 'tone_changer.md')
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()

    async def execute(self, input_data: Any) -> AgentOutput:
        start_time = time.time()
        logs = [f"Started {self.name}"]
        
        # Validate Input
        try:
            if isinstance(input_data, dict):
                validated_input = ToneChangerInput(**input_data)
            else:
                validated_input = ToneChangerInput(text=str(input_data))
        except Exception as e:
            return AgentOutput(
                status="failed",
                execution_time=round(time.time() - start_time, 2),
                agent_name=self.name,
                category=self.category,
                output=f"Validation Error: {e}",
                logs=logs + ["Failed during validation"]
            )
            
        logs.append("Preparing Prompt")
        self.system_prompt = self._load_prompt()
        
        # Format the system prompt if there are variables
        if "ToneChangerAgent" == "SummarizerAgent":
            self.system_prompt = self.system_prompt.replace("{length}", validated_input.length.value)
        elif "ToneChangerAgent" == "ToneChangerAgent":
            self.system_prompt = self.system_prompt.replace("{tone}", validated_input.tone.value)
        elif "ToneChangerAgent" == "TranslatorAgent":
            self.system_prompt = self.system_prompt.replace("{target_language}", getattr(validated_input, 'target_language', 'English'))
        elif "ToneChangerAgent" == "TitleGeneratorAgent":
            self.system_prompt = self.system_prompt.replace("{context}", validated_input.context.value)
        elif "ToneChangerAgent" == "EmailWriterAgent":
            self.system_prompt = self.system_prompt.replace("{purpose}", getattr(validated_input, 'purpose', ''))
            self.system_prompt = self.system_prompt.replace("{recipient}", getattr(validated_input, 'recipient', ''))
            self.system_prompt = self.system_prompt.replace("{tone}", validated_input.tone.value)
            self.system_prompt = self.system_prompt.replace("{text}", getattr(validated_input, 'text', ''))
        elif "ToneChangerAgent" == "QuestionGeneratorAgent":
            self.system_prompt = self.system_prompt.replace("{question_type}", validated_input.question_type.value)
        elif "ToneChangerAgent" == "TextSimplifierAgent":
            self.system_prompt = self.system_prompt.replace("{reading_level}", validated_input.reading_level.value)

        user_prompt = getattr(validated_input, 'text', str(input_data))
        
        logs.append("Calling Groq")
        response = await self.generate_response(user_prompt)
        
        logs.append("Receiving Response")
        logs.append("Completed")
        
        return AgentOutput(
            status="success",
            execution_time=round(time.time() - start_time, 2),
            agent_name=self.name,
            category=self.category,
            output=response,
            logs=logs
        )
