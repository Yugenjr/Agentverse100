from typing import Any
import os
import time
from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput
from app.schemas.student_assistant_schemas import MCQGeneratorInput

class MCQGeneratorAgent(BaseAgent):
    name = "MCQ Generator"
    description = "Generate Multiple Choice Questions."
    category = "Student Assistant"
    icon = "ListChecks"
    
    def _load_prompt(self) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'prompts', 'student_assistant', 'mcq_generator.md')
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()

    async def execute(self, input_data: Any) -> AgentOutput:
        start_time = time.time()
        logs = [f"Started {self.name}"]
        
        # Validate Input
        try:
            if isinstance(input_data, dict):
                validated_input = MCQGeneratorInput(**input_data)
            else:
                raise ValueError("Expected dictionary input for Student Assistant agents")
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
        
        self.system_prompt = self.system_prompt.replace('{{ topic }}', str(getattr(validated_input, 'topic', '')))
        self.system_prompt = self.system_prompt.replace('{{ count }}', str(getattr(validated_input, 'count', '')))

        
        user_prompt = "Please execute your task based on the provided inputs."
        
        logs.append("Sending to Groq")
        response = await self.generate_response(user_prompt)
        
        logs.append("Receiving Response")
        logs.append("Formatting Output")
        logs.append("Completed")
        
        return AgentOutput(
            status="success",
            execution_time=round(time.time() - start_time, 2),
            agent_name=self.name,
            category=self.category,
            output=response,
            logs=logs
        )
