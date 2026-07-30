from pydantic import BaseModel, Field, constr
from typing import Optional
from enum import Enum

class SummaryLength(str, Enum):
    SHORT = "Short"
    MEDIUM = "Medium"
    DETAILED = "Detailed"

class ToneOption(str, Enum):
    FORMAL = "Formal"
    CASUAL = "Casual"
    PROFESSIONAL = "Professional"
    FRIENDLY = "Friendly"
    ACADEMIC = "Academic"

class TitleContext(str, Enum):
    PROFESSIONAL = "Professional"
    BLOG = "Blog"
    SEO = "SEO"
    ACADEMIC = "Academic"
    MARKETING = "Marketing"

class QuestionType(str, Enum):
    MCQ = "MCQ"
    SHORT_ANSWER = "Short Answer"
    INTERVIEW = "Interview"
    QUIZ = "Quiz"
    DISCUSSION = "Discussion"

class ReadingLevel(str, Enum):
    CHILD = "Child"
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    EXPERT = "Expert"

class BaseTextProcessingInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=50000, description="The text to process.")

class SummarizerInput(BaseTextProcessingInput):
    length: SummaryLength = Field(default=SummaryLength.MEDIUM)

class GrammarFixerInput(BaseTextProcessingInput):
    pass

class ToneChangerInput(BaseTextProcessingInput):
    tone: ToneOption = Field(default=ToneOption.PROFESSIONAL)

class TranslatorInput(BaseTextProcessingInput):
    target_language: str = Field(..., min_length=2, max_length=50, description="The language to translate to.")

class KeywordExtractorInput(BaseTextProcessingInput):
    pass

class BulletPointGeneratorInput(BaseTextProcessingInput):
    pass

class TitleGeneratorInput(BaseTextProcessingInput):
    context: TitleContext = Field(default=TitleContext.BLOG)

class EmailWriterInput(BaseModel):
    purpose: str = Field(..., min_length=1, max_length=500)
    recipient: str = Field(..., min_length=1, max_length=100)
    tone: ToneOption = Field(default=ToneOption.PROFESSIONAL)
    text: Optional[str] = Field(default="", max_length=50000, description="Additional context or text to include.")

class QuestionGeneratorInput(BaseTextProcessingInput):
    question_type: QuestionType = Field(default=QuestionType.MCQ)

class TextSimplifierInput(BaseTextProcessingInput):
    reading_level: ReadingLevel = Field(default=ReadingLevel.BEGINNER)
