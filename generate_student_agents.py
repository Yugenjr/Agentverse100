import os

agents = [
    {
        "class_name": "NotesGeneratorAgent",
        "name": "Notes Generator",
        "desc": "Generate clean study notes from any topic.",
        "icon": "FileText",
        "input_model": "NotesGeneratorInput",
        "prompt_file": "notes_generator.md",
        "file_name": "notes_generator_agent.py",
        "vars": ["topic", "notes_type"]
    },
    {
        "class_name": "FlashcardGeneratorAgent",
        "name": "Flashcard Generator",
        "desc": "Convert topics into study flashcards.",
        "icon": "Layers",
        "input_model": "FlashcardGeneratorInput",
        "prompt_file": "flashcard_generator.md",
        "file_name": "flashcard_generator_agent.py",
        "vars": ["topic"]
    },
    {
        "class_name": "QuizGeneratorAgent",
        "name": "Quiz Generator",
        "desc": "Generate quizzes with explanations.",
        "icon": "HelpCircle",
        "input_model": "QuizGeneratorInput",
        "prompt_file": "quiz_generator.md",
        "file_name": "quiz_generator_agent.py",
        "vars": ["topic", "difficulty"]
    },
    {
        "class_name": "MCQGeneratorAgent",
        "name": "MCQ Generator",
        "desc": "Generate Multiple Choice Questions.",
        "icon": "ListChecks",
        "input_model": "MCQGeneratorInput",
        "prompt_file": "mcq_generator.md",
        "file_name": "mcq_generator_agent.py",
        "vars": ["topic", "count"]
    },
    {
        "class_name": "AssignmentHelperAgent",
        "name": "Assignment Helper",
        "desc": "Help students structure assignments.",
        "icon": "PenTool",
        "input_model": "AssignmentHelperInput",
        "prompt_file": "assignment_helper.md",
        "file_name": "assignment_helper_agent.py",
        "vars": ["topic", "academic_level"]
    },
    {
        "class_name": "ConceptExplainerAgent",
        "name": "Concept Explainer",
        "desc": "Explain difficult concepts simply.",
        "icon": "Lightbulb",
        "input_model": "ConceptExplainerInput",
        "prompt_file": "concept_explainer.md",
        "file_name": "concept_explainer_agent.py",
        "vars": ["concept", "audience"]
    },
    {
        "class_name": "RoadmapPlannerAgent",
        "name": "Roadmap Planner",
        "desc": "Generate personalized learning roadmaps.",
        "icon": "Map",
        "input_model": "RoadmapPlannerInput",
        "prompt_file": "roadmap_planner.md",
        "file_name": "roadmap_planner_agent.py",
        "vars": ["topic", "duration_weeks", "daily_hours"]
    },
    {
        "class_name": "FormulaSheetGeneratorAgent",
        "name": "Formula Sheet Generator",
        "desc": "Generate formula sheets for math, physics, etc.",
        "icon": "Sigma",
        "input_model": "FormulaSheetGeneratorInput",
        "prompt_file": "formula_sheet_generator.md",
        "file_name": "formula_sheet_generator_agent.py",
        "vars": ["subject", "specific_topic"]
    },
    {
        "class_name": "VivaPreparationAgent",
        "name": "Viva Preparation",
        "desc": "Generate viva questions and follow-ups.",
        "icon": "MessageCircle",
        "input_model": "VivaPreparationInput",
        "prompt_file": "viva_preparation.md",
        "file_name": "viva_preparation_agent.py",
        "vars": ["topic", "level"]
    },
    {
        "class_name": "RevisionPlannerAgent",
        "name": "Revision Planner",
        "desc": "Create day-wise revision schedules.",
        "icon": "Calendar",
        "input_model": "RevisionPlannerInput",
        "prompt_file": "revision_planner.md",
        "file_name": "revision_planner_agent.py",
        "vars": ["exam_date", "subjects", "daily_study_hours"]
    }
]

template = """from typing import Any
import os
import time
from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput
from app.schemas.student_assistant_schemas import {input_model}

class {class_name}(BaseAgent):
    name = "{name}"
    description = "{desc}"
    category = "Student Assistant"
    icon = "{icon}"
    
    def _load_prompt(self) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'prompts', 'student_assistant', '{prompt_file}')
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()

    async def execute(self, input_data: Any) -> AgentOutput:
        start_time = time.time()
        logs = [f"Started {{self.name}}"]
        
        # Validate Input
        try:
            if isinstance(input_data, dict):
                validated_input = {input_model}(**input_data)
            else:
                raise ValueError("Expected dictionary input for Student Assistant agents")
        except Exception as e:
            return AgentOutput(
                status="failed",
                execution_time=round(time.time() - start_time, 2),
                agent_name=self.name,
                category=self.category,
                output=f"Validation Error: {{e}}",
                logs=logs + ["Failed during validation"]
            )
            
        logs.append("Preparing Prompt")
        self.system_prompt = self._load_prompt()
        
{replacements}
        
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
"""

os.makedirs('backend/app/agents/categories/student_assistant', exist_ok=True)
for agent in agents:
    reps = ""
    for v in agent['vars']:
        reps += f"        self.system_prompt = self.system_prompt.replace('{{{{ {v} }}}}', str(getattr(validated_input, '{v}', '')))\n"
    
    content = template.format(
        class_name=agent['class_name'],
        name=agent['name'],
        desc=agent['desc'],
        icon=agent['icon'],
        input_model=agent['input_model'],
        prompt_file=agent['prompt_file'],
        replacements=reps
    )
    
    with open(f"backend/app/agents/categories/student_assistant/{agent['file_name']}", 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated 10 student assistant agents!")
