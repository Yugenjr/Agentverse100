from pydantic import BaseModel, Field

class DatasetAnalyzerInput(BaseModel):
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")
    features: str = Field(..., min_length=1, description="List of main features in the dataset")

class DataCleaningAdvisorInput(BaseModel):
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")

class FeatureEngineeringInput(BaseModel):
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")
    target_column: str = Field(..., min_length=1, description="The target variable to predict")

class MachineLearningModelRecommenderInput(BaseModel):
    ml_task: str = Field(default="Classification", description="Task type: Classification, Regression, or Clustering")
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")

class ModelEvaluationInput(BaseModel):
    ml_task: str = Field(default="Classification", description="Task type")
    evaluation_metric: str = Field(..., min_length=1, description="Primary evaluation metric (e.g., Accuracy, RMSE)")

class FeatureImportanceInput(BaseModel):
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")
    ml_task: str = Field(default="Classification", description="Task type")

class DataVisualizationAdvisorInput(BaseModel):
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")
    features: str = Field(..., min_length=1, description="Key features to visualize")

class OutlierDetectionInput(BaseModel):
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")

class DriftDetectionAdvisorInput(BaseModel):
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")
    problem_statement: str = Field(..., min_length=1, description="The ML problem being solved")

class MLPipelineGeneratorInput(BaseModel):
    problem_statement: str = Field(..., min_length=1, description="The ML problem to solve")
    dataset_description: str = Field(..., min_length=1, description="Description of the dataset")
