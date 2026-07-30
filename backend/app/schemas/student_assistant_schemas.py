from pydantic import BaseModel, Field

class NotesGeneratorInput(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic to generate notes for")
    notes_type: str = Field(default="Detailed Notes", description="Type of notes: Short Notes, Detailed Notes, Revision Notes")

class FlashcardGeneratorInput(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic to create flashcards for")

class QuizGeneratorInput(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic of the quiz")
    difficulty: str = Field(default="Medium", description="Difficulty: Easy, Medium, Hard")

class MCQGeneratorInput(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic of the MCQs")
    count: int = Field(default=10, description="Number of questions (5, 10, 20, 50)")

class AssignmentHelperInput(BaseModel):
    topic: str = Field(..., min_length=1, description="Assignment topic")
    academic_level: str = Field(default="College Student", description="Academic level")

class ConceptExplainerInput(BaseModel):
    concept: str = Field(..., min_length=1, description="Concept to explain")
    audience: str = Field(default="Beginner", description="Target audience: Child, Beginner, College Student, Professional")

class RoadmapPlannerInput(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic to learn")
    duration_weeks: int = Field(default=4, description="Duration in weeks")
    daily_hours: float = Field(default=2.0, description="Daily study hours")

class FormulaSheetGeneratorInput(BaseModel):
    subject: str = Field(..., min_length=1, description="Subject (Mathematics, Physics, Statistics, Machine Learning, Engineering)")
    specific_topic: str = Field(default="General", description="Specific topic within the subject")

class VivaPreparationInput(BaseModel):
    topic: str = Field(..., min_length=1, description="Topic for viva")
    level: str = Field(default="Intermediate", description="Level: Basic, Intermediate, Advanced")

class RevisionPlannerInput(BaseModel):
    exam_date: str = Field(..., min_length=1, description="Date of the exam")
    subjects: str = Field(..., min_length=1, description="Comma separated list of subjects")
    daily_study_hours: float = Field(default=4.0, description="Daily study hours allocated for revision")
