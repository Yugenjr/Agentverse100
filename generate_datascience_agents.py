import os

agents = [
    {
        "class_name": "DatasetAnalyzerAgent",
        "name": "Dataset Analyzer",
        "desc": "Analyze datasets and get an overview.",
        "icon": "Table2",
        "input_model": "DatasetAnalyzerInput",
        "prompt_file": "dataset_analyzer.md",
        "file_name": "dataset_analyzer_agent.py",
        "vars": ["dataset_description", "features"]
    },
    {
        "class_name": "DataCleaningAdvisorAgent",
        "name": "Data Cleaning Advisor",
        "desc": "Recommend data cleaning strategies.",
        "icon": "Brush",
        "input_model": "DataCleaningAdvisorInput",
        "prompt_file": "data_cleaning.md",
        "file_name": "data_cleaning_advisor_agent.py",
        "vars": ["dataset_description"]
    },
    {
        "class_name": "FeatureEngineeringAgent",
        "name": "Feature Engineering",
        "desc": "Suggest feature engineering techniques.",
        "icon": "Wrench",
        "input_model": "FeatureEngineeringInput",
        "prompt_file": "feature_engineering.md",
        "file_name": "feature_engineering_agent.py",
        "vars": ["dataset_description", "target_column"]
    },
    {
        "class_name": "MachineLearningModelRecommenderAgent",
        "name": "ML Model Recommender",
        "desc": "Recommend ML algorithms based on the dataset.",
        "icon": "Brain",
        "input_model": "MachineLearningModelRecommenderInput",
        "prompt_file": "model_recommender.md",
        "file_name": "model_recommender_agent.py",
        "vars": ["ml_task", "dataset_description"]
    },
    {
        "class_name": "ModelEvaluationAgent",
        "name": "Model Evaluation",
        "desc": "Evaluate ML models with proper metrics.",
        "icon": "CheckCircle2",
        "input_model": "ModelEvaluationInput",
        "prompt_file": "evaluation.md",
        "file_name": "model_evaluation_agent.py",
        "vars": ["ml_task", "evaluation_metric"]
    },
    {
        "class_name": "FeatureImportanceAgent",
        "name": "Feature Importance",
        "desc": "Explain and suggest feature importance techniques.",
        "icon": "BarChart3",
        "input_model": "FeatureImportanceInput",
        "prompt_file": "feature_importance.md",
        "file_name": "feature_importance_agent.py",
        "vars": ["dataset_description", "ml_task"]
    },
    {
        "class_name": "DataVisualizationAdvisorAgent",
        "name": "Data Visualization Advisor",
        "desc": "Recommend visualizations for the dataset.",
        "icon": "PieChart",
        "input_model": "DataVisualizationAdvisorInput",
        "prompt_file": "visualization.md",
        "file_name": "visualization_advisor_agent.py",
        "vars": ["dataset_description", "features"]
    },
    {
        "class_name": "OutlierDetectionAgent",
        "name": "Outlier Detection",
        "desc": "Identify and handle outliers.",
        "icon": "Target",
        "input_model": "OutlierDetectionInput",
        "prompt_file": "outlier_detection.md",
        "file_name": "outlier_detection_agent.py",
        "vars": ["dataset_description"]
    },
    {
        "class_name": "DriftDetectionAdvisorAgent",
        "name": "Drift Detection Advisor",
        "desc": "Analyze possible data and concept drift.",
        "icon": "Activity",
        "input_model": "DriftDetectionAdvisorInput",
        "prompt_file": "drift.md",
        "file_name": "drift_detection_advisor_agent.py",
        "vars": ["dataset_description", "problem_statement"]
    },
    {
        "class_name": "MLPipelineGeneratorAgent",
        "name": "ML Pipeline Generator",
        "desc": "Generate complete ML workflows from data to deployment.",
        "icon": "GitMerge",
        "input_model": "MLPipelineGeneratorInput",
        "prompt_file": "pipeline.md",
        "file_name": "ml_pipeline_generator_agent.py",
        "vars": ["problem_statement", "dataset_description"]
    }
]

template = """from typing import Any
import os
import time
from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput
from app.schemas.datascience_schemas import {input_model}

class {class_name}(BaseAgent):
    name = "{name}"
    description = "{desc}"
    category = "Data Science"
    icon = "{icon}"
    
    def _load_prompt(self) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'prompts', 'datascience', '{prompt_file}')
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
                raise ValueError("Expected dictionary input for Data Science agents")
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
        
        logs.append("Calling Groq")
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

os.makedirs('backend/app/agents/categories/data_science', exist_ok=True)
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
    
    with open(f"backend/app/agents/categories/data_science/{agent['file_name']}", 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated 10 data science agents!")
