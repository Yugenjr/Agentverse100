import os

agents = [
    {
        "class_name": "BusinessPlanGeneratorAgent",
        "name": "Business Plan Generator",
        "desc": "Generate complete startup business plans.",
        "icon": "Briefcase",
        "input_model": "BusinessPlanGeneratorInput",
        "prompt_file": "business_plan.md",
        "file_name": "business_plan_agent.py",
        "vars": ["business_idea", "target_market"]
    },
    {
        "class_name": "SWOTAnalysisAgent",
        "name": "SWOT Analysis",
        "desc": "Generate Strengths, Weaknesses, Opportunities, and Threats for any business idea.",
        "icon": "Target",
        "input_model": "SWOTAnalysisInput",
        "prompt_file": "swot.md",
        "file_name": "swot_analysis_agent.py",
        "vars": ["business_idea"]
    },
    {
        "class_name": "CompetitorAnalysisAgent",
        "name": "Competitor Analysis",
        "desc": "Analyze competitors and market position.",
        "icon": "Users",
        "input_model": "CompetitorAnalysisInput",
        "prompt_file": "competitor_analysis.md",
        "file_name": "competitor_analysis_agent.py",
        "vars": ["industry", "competitor_names"]
    },
    {
        "class_name": "CustomerPersonaAgent",
        "name": "Customer Persona",
        "desc": "Generate customer personas with pain points and buying behavior.",
        "icon": "UserCircle",
        "input_model": "CustomerPersonaInput",
        "prompt_file": "customer_persona.md",
        "file_name": "customer_persona_agent.py",
        "vars": ["product_description", "target_market"]
    },
    {
        "class_name": "MarketResearchAgent",
        "name": "Market Research",
        "desc": "Provide industry overview, market size, and trends.",
        "icon": "LineChart",
        "input_model": "MarketResearchInput",
        "prompt_file": "market_research.md",
        "file_name": "market_research_agent.py",
        "vars": ["industry", "country"]
    },
    {
        "class_name": "RevenueModelAgent",
        "name": "Revenue Model",
        "desc": "Suggest revenue models like SaaS, Commission, etc.",
        "icon": "DollarSign",
        "input_model": "RevenueModelInput",
        "prompt_file": "revenue_model.md",
        "file_name": "revenue_model_agent.py",
        "vars": ["business_idea", "startup_stage"]
    },
    {
        "class_name": "PricingStrategyAgent",
        "name": "Pricing Strategy",
        "desc": "Recommend pricing strategies like Value Based, Cost Plus, etc.",
        "icon": "Tags",
        "input_model": "PricingStrategyInput",
        "prompt_file": "pricing.md",
        "file_name": "pricing_strategy_agent.py",
        "vars": ["product_description", "target_market"]
    },
    {
        "class_name": "RiskAssessmentAgent",
        "name": "Risk Assessment",
        "desc": "Identify technical, financial, operational, and legal risks.",
        "icon": "AlertTriangle",
        "input_model": "RiskAssessmentInput",
        "prompt_file": "risk_assessment.md",
        "file_name": "risk_assessment_agent.py",
        "vars": ["business_idea", "industry"]
    },
    {
        "class_name": "PitchDeckGeneratorAgent",
        "name": "Pitch Deck Generator",
        "desc": "Generate startup pitch deck content.",
        "icon": "Presentation",
        "input_model": "PitchDeckGeneratorInput",
        "prompt_file": "pitch_deck.md",
        "file_name": "pitch_deck_generator_agent.py",
        "vars": ["business_idea", "funding_required"]
    },
    {
        "class_name": "ProposalWriterAgent",
        "name": "Proposal Writer",
        "desc": "Generate professional business proposals.",
        "icon": "FileSignature",
        "input_model": "ProposalWriterInput",
        "prompt_file": "proposal.md",
        "file_name": "proposal_writer_agent.py",
        "vars": ["project_description", "proposal_type"]
    }
]

template = """from typing import Any
import os
import time
from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput
from app.schemas.business_schemas import {input_model}

class {class_name}(BaseAgent):
    name = "{name}"
    description = "{desc}"
    category = "Business"
    icon = "{icon}"
    
    def _load_prompt(self) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'prompts', 'business', '{prompt_file}')
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
                raise ValueError("Expected dictionary input for Business agents")
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

os.makedirs('backend/app/agents/categories/business', exist_ok=True)
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
    
    with open(f"backend/app/agents/categories/business/{agent['file_name']}", 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated 10 business agents!")
