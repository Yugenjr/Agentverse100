from pydantic import BaseModel, Field

class CodeReviewInput(BaseModel):
    language: str = Field(..., min_length=1, description="Programming language of the source code")
    source_code: str = Field(..., min_length=1, description="Source code to review")

class BugFinderInput(BaseModel):
    language: str = Field(..., min_length=1, description="Programming language of the source code")
    source_code: str = Field(..., min_length=1, description="Source code to analyze for bugs")

class RefactoringInput(BaseModel):
    language: str = Field(..., min_length=1, description="Programming language of the source code")
    source_code: str = Field(..., min_length=1, description="Source code to refactor")

class CodeExplainerInput(BaseModel):
    language: str = Field(..., min_length=1, description="Programming language of the source code")
    source_code: str = Field(..., min_length=1, description="Source code to explain")
    level: str = Field(default="Intermediate", description="Explanation level: Beginner, Intermediate, or Expert")

class ComplexityAnalyzerInput(BaseModel):
    language: str = Field(..., min_length=1, description="Programming language of the source code")
    source_code: str = Field(..., min_length=1, description="Source code to analyze")

class TestCaseGeneratorInput(BaseModel):
    language: str = Field(..., min_length=1, description="Programming language of the source code")
    source_code: str = Field(..., min_length=1, description="Source code to generate tests for")

class APIDesignerInput(BaseModel):
    description: str = Field(..., min_length=10, description="Description of the API to design")

class SQLOptimizerInput(BaseModel):
    sql_query: str = Field(..., min_length=5, description="SQL query to optimize")
    schema_context: str = Field(default="", description="Optional database schema context")

class DocumentationGeneratorInput(BaseModel):
    language: str = Field(..., min_length=1, description="Programming language of the source code")
    source_code: str = Field(..., min_length=1, description="Source code to generate documentation for")
    doc_type: str = Field(default="Function Docs", description="Type of docs: README, API Docs, Function Docs, etc.")

class GitCommitGeneratorInput(BaseModel):
    diff: str = Field(..., min_length=5, description="Git diff output")
    commit_type: str = Field(default="Feature", description="Type: Feature, Bug Fix, Refactor, Docs, Chore")
