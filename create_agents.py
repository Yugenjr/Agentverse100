import os
import glob

# Delete old files
directory = 'backend/app/agents/categories/text_processing'
for f in glob.glob(f"{directory}/*.py"):
    if not f.endswith('__init__.py'):
        os.remove(f)

# The list of agents
agents = [
    {
        "filename": "summarizer_agent.py",
        "classname": "SummarizerAgent",
        "name": "Summarizer",
        "description": "Summarize long text with options for Short, Medium, or Detailed summaries.",
        "icon": "FileText",
        "prompt_file": "summarizer.md",
        "schema": "SummarizerInput"
    },
    {
        "filename": "grammar_fixer_agent.py",
        "classname": "GrammarFixerAgent",
        "name": "Grammar Fixer",
        "description": "Correct grammar and spelling while preserving meaning.",
        "icon": "CheckCircle",
        "prompt_file": "grammar_fixer.md",
        "schema": "GrammarFixerInput"
    },
    {
        "filename": "tone_changer_agent.py",
        "classname": "ToneChangerAgent",
        "name": "Tone Changer",
        "description": "Rewrite text to match Formal, Casual, Professional, Friendly, or Academic tones.",
        "icon": "MessageSquare",
        "prompt_file": "tone_changer.md",
        "schema": "ToneChangerInput"
    },
    {
        "filename": "translator_agent.py",
        "classname": "TranslatorAgent",
        "name": "Translator",
        "description": "Translate text between languages seamlessly.",
        "icon": "Languages",
        "prompt_file": "translator.md",
        "schema": "TranslatorInput"
    },
    {
        "filename": "keyword_extractor_agent.py",
        "classname": "KeywordExtractorAgent",
        "name": "Keyword Extractor",
        "description": "Extract important keywords and return relevance scores.",
        "icon": "Key",
        "prompt_file": "keyword_extractor.md",
        "schema": "KeywordExtractorInput"
    },
    {
        "filename": "bullet_point_generator_agent.py",
        "classname": "BulletPointGeneratorAgent",
        "name": "Bullet Point Generator",
        "description": "Convert paragraphs into structured bullet points.",
        "icon": "List",
        "prompt_file": "bullet_point_generator.md",
        "schema": "BulletPointGeneratorInput"
    },
    {
        "filename": "title_generator_agent.py",
        "classname": "TitleGeneratorAgent",
        "name": "Title Generator",
        "description": "Generate engaging titles for Blogs, SEO, Marketing, and Academic use.",
        "icon": "Type",
        "prompt_file": "title_generator.md",
        "schema": "TitleGeneratorInput"
    },
    {
        "filename": "email_writer_agent.py",
        "classname": "EmailWriterAgent",
        "name": "Email Writer",
        "description": "Generate professional emails based on purpose and recipient.",
        "icon": "Mail",
        "prompt_file": "email_writer.md",
        "schema": "EmailWriterInput"
    },
    {
        "filename": "question_generator_agent.py",
        "classname": "QuestionGeneratorAgent",
        "name": "Question Generator",
        "description": "Generate questions for quizzes, interviews, and discussions.",
        "icon": "HelpCircle",
        "prompt_file": "question_generator.md",
        "schema": "QuestionGeneratorInput"
    },
    {
        "filename": "text_simplifier_agent.py",
        "classname": "TextSimplifierAgent",
        "name": "Text Simplifier",
        "description": "Rewrite difficult text for different reading levels.",
        "icon": "Feather",
        "prompt_file": "text_simplifier.md",
        "schema": "TextSimplifierInput"
    }
]

template = """from typing import Any
import os
import time
from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput
from app.schemas.text_processing_schemas import {schema}

class {classname}(BaseAgent):
    name = "{name}"
    description = "{description}"
    category = "Text Processing"
    icon = "{icon}"
    
    def _load_prompt(self) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'prompts', 'text_processing', '{prompt_file}')
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()

    async def execute(self, input_data: Any) -> AgentOutput:
        start_time = time.time()
        logs = [f"Started {{self.name}}"]
        
        # Validate Input
        try:
            if isinstance(input_data, dict):
                validated_input = {schema}(**input_data)
            else:
                validated_input = {schema}(text=str(input_data))
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
        
        # Format the system prompt if there are variables
        if "{classname}" == "SummarizerAgent":
            self.system_prompt = self.system_prompt.replace("{{length}}", validated_input.length.value)
        elif "{classname}" == "ToneChangerAgent":
            self.system_prompt = self.system_prompt.replace("{{tone}}", validated_input.tone.value)
        elif "{classname}" == "TranslatorAgent":
            self.system_prompt = self.system_prompt.replace("{{target_language}}", getattr(validated_input, 'target_language', 'English'))
        elif "{classname}" == "TitleGeneratorAgent":
            self.system_prompt = self.system_prompt.replace("{{context}}", validated_input.context.value)
        elif "{classname}" == "EmailWriterAgent":
            self.system_prompt = self.system_prompt.replace("{{purpose}}", getattr(validated_input, 'purpose', ''))
            self.system_prompt = self.system_prompt.replace("{{recipient}}", getattr(validated_input, 'recipient', ''))
            self.system_prompt = self.system_prompt.replace("{{tone}}", validated_input.tone.value)
            self.system_prompt = self.system_prompt.replace("{{text}}", getattr(validated_input, 'text', ''))
        elif "{classname}" == "QuestionGeneratorAgent":
            self.system_prompt = self.system_prompt.replace("{{question_type}}", validated_input.question_type.value)
        elif "{classname}" == "TextSimplifierAgent":
            self.system_prompt = self.system_prompt.replace("{{reading_level}}", validated_input.reading_level.value)

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
"""

for agent in agents:
    filepath = os.path.join(directory, agent["filename"])
    content = template.format(
        classname=agent["classname"],
        name=agent["name"],
        description=agent["description"],
        icon=agent["icon"],
        prompt_file=agent["prompt_file"],
        schema=agent["schema"]
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Created 10 agents successfully.")
