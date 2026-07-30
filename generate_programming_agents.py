import os

agents = [
    {
        "class_name": "CodeReviewerAgent",
        "name": "Code Reviewer",
        "desc": "Reviews source code for quality, best practices, and readability.",
        "icon": "Code",
        "input_model": "CodeReviewInput",
        "prompt_file": "code_review.md",
        "file_name": "code_reviewer_agent.py",
        "vars": ["language", "source_code"]
    },
    {
        "class_name": "BugFinderAgent",
        "name": "Bug Finder",
        "desc": "Analyze code to identify logical, syntax, runtime, and hidden bugs.",
        "icon": "Bug",
        "input_model": "BugFinderInput",
        "prompt_file": "bug_finder.md",
        "file_name": "bug_finder_agent.py",
        "vars": ["language", "source_code"]
    },
    {
        "class_name": "RefactoringAgent",
        "name": "Refactoring Agent",
        "desc": "Improves existing code structure without changing functionality.",
        "icon": "Wrench",
        "input_model": "RefactoringInput",
        "prompt_file": "refactor.md",
        "file_name": "refactoring_agent.py",
        "vars": ["language", "source_code"]
    },
    {
        "class_name": "CodeExplainerAgent",
        "name": "Code Explainer",
        "desc": "Explains unfamiliar code step-by-step for different skill levels.",
        "icon": "BookOpen",
        "input_model": "CodeExplainerInput",
        "prompt_file": "code_explainer.md",
        "file_name": "code_explainer_agent.py",
        "vars": ["language", "source_code", "level"]
    },
    {
        "class_name": "ComplexityAnalyzerAgent",
        "name": "Complexity Analyzer",
        "desc": "Analyzes algorithm time and space complexity with optimization suggestions.",
        "icon": "Activity",
        "input_model": "ComplexityAnalyzerInput",
        "prompt_file": "complexity.md",
        "file_name": "complexity_analyzer_agent.py",
        "vars": ["language", "source_code"]
    },
    {
        "class_name": "TestCaseGeneratorAgent",
        "name": "Test Case Generator",
        "desc": "Generates unit tests, edge cases, and boundary tests for functions.",
        "icon": "TestTube2",
        "input_model": "TestCaseGeneratorInput",
        "prompt_file": "test_case_generator.md",
        "file_name": "test_case_generator_agent.py",
        "vars": ["language", "source_code"]
    },
    {
        "class_name": "APIDesignerAgent",
        "name": "API Designer",
        "desc": "Designs REST APIs including endpoints, models, and status codes.",
        "icon": "Network",
        "input_model": "APIDesignerInput",
        "prompt_file": "api_designer.md",
        "file_name": "api_designer_agent.py",
        "vars": ["description"]
    },
    {
        "class_name": "SQLOptimizerAgent",
        "name": "SQL Query Optimizer",
        "desc": "Improves SQL queries by optimizing joins, indexes, and redundancy.",
        "icon": "Database",
        "input_model": "SQLOptimizerInput",
        "prompt_file": "sql_optimizer.md",
        "file_name": "sql_optimizer_agent.py",
        "vars": ["sql_query", "schema_context"]
    },
    {
        "class_name": "DocumentationGeneratorAgent",
        "name": "Documentation Generator",
        "desc": "Generates READMEs, API docs, function docs, and usage examples.",
        "icon": "FileCode2",
        "input_model": "DocumentationGeneratorInput",
        "prompt_file": "documentation.md",
        "file_name": "documentation_generator_agent.py",
        "vars": ["language", "source_code", "doc_type"]
    },
    {
        "class_name": "GitCommitGeneratorAgent",
        "name": "Git Commit Generator",
        "desc": "Generates professional Conventional Commits based on code diffs.",
        "icon": "GitCommit",
        "input_model": "GitCommitGeneratorInput",
        "prompt_file": "git_commit.md",
        "file_name": "git_commit_generator_agent.py",
        "vars": ["diff", "commit_type"]
    }
]

template = """from typing import Any
import os
import time
from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput
from app.schemas.programming_schemas import {input_model}

class {class_name}(BaseAgent):
    name = "{name}"
    description = "{desc}"
    category = "Programming"
    icon = "{icon}"
    
    def _load_prompt(self) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'prompts', 'programming', '{prompt_file}')
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
                raise ValueError("Expected dictionary input for Programming agents")
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

os.makedirs('backend/app/agents/categories/programming', exist_ok=True)
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
    
    with open(f"backend/app/agents/categories/programming/{agent['file_name']}", 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated 10 programming agents!")
