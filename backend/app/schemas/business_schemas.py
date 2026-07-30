from pydantic import BaseModel, Field

class BusinessPlanGeneratorInput(BaseModel):
    business_idea: str = Field(..., min_length=1, description="The business idea or concept")
    target_market: str = Field(..., min_length=1, description="The target market or audience")

class SWOTAnalysisInput(BaseModel):
    business_idea: str = Field(..., min_length=1, description="The business idea to analyze")

class CompetitorAnalysisInput(BaseModel):
    industry: str = Field(..., min_length=1, description="Industry or sector")
    competitor_names: str = Field(..., min_length=1, description="Comma separated list of competitors")

class CustomerPersonaInput(BaseModel):
    product_description: str = Field(..., min_length=1, description="Description of the product or service")
    target_market: str = Field(..., min_length=1, description="The target market")

class MarketResearchInput(BaseModel):
    industry: str = Field(..., min_length=1, description="Industry to research")
    country: str = Field(default="Global", description="Target country or region")

class RevenueModelInput(BaseModel):
    business_idea: str = Field(..., min_length=1, description="The business idea")
    startup_stage: str = Field(default="Idea", description="Current stage of the startup")

class PricingStrategyInput(BaseModel):
    product_description: str = Field(..., min_length=1, description="Description of the product")
    target_market: str = Field(..., min_length=1, description="Target audience")

class RiskAssessmentInput(BaseModel):
    business_idea: str = Field(..., min_length=1, description="The business idea")
    industry: str = Field(..., min_length=1, description="Industry")

class PitchDeckGeneratorInput(BaseModel):
    business_idea: str = Field(..., min_length=1, description="The business idea")
    funding_required: str = Field(..., min_length=1, description="Amount of funding required")

class ProposalWriterInput(BaseModel):
    project_description: str = Field(..., min_length=1, description="Description of the project or partnership")
    proposal_type: str = Field(default="Client Proposal", description="Type of proposal")
