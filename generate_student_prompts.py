import os

prompts = {
    "notes_generator.md": """You are an expert Notes Generator Agent.
Your task is to generate clean study notes for the following topic.

Topic: {{ topic }}
Type of Notes: {{ notes_type }}

Provide:
1. Structured Headings
2. Key Concepts and Definitions
3. Important bullet points
4. Summary or Conclusion
Ensure the notes match the requested type (Short, Detailed, or Revision).""",

    "flashcard_generator.md": """You are an expert Flashcard Generator Agent.
Your task is to convert the following topic into study flashcards.

Topic: {{ topic }}

For each flashcard, provide:
- Question
- Answer
- Difficulty (Easy, Medium, Hard)""",

    "quiz_generator.md": """You are an expert Quiz Generator Agent.
Your task is to generate a quiz on the following topic.

Topic: {{ topic }}
Difficulty: {{ difficulty }}

For each question, provide:
- The Question
- 4 Multiple Choice Options (A, B, C, D)
- The Correct Answer
- A brief Explanation of why it is correct""",

    "mcq_generator.md": """You are an expert MCQ Generator Agent.
Your task is to generate exactly {{ count }} Multiple Choice Questions for the following topic.

Topic: {{ topic }}

For each question, provide:
- The Question
- 4 Options
- The Correct Answer""",

    "assignment_helper.md": """You are an expert Assignment Helper Agent.
Your task is to help structure an assignment for the following topic.

Topic: {{ topic }}
Academic Level: {{ academic_level }}

Generate a structured outline including:
1. Introduction (Key hook and thesis)
2. Objectives (What the assignment will cover)
3. Content Outline (Main headings and subheadings)
4. Conclusion (Summary of key points)
5. References Suggestions (Types of sources to look for)""",

    "concept_explainer.md": """You are an expert Concept Explainer Agent.
Your task is to explain the following difficult concept.

Concept: {{ concept }}
Target Audience: {{ audience }}

Explain the concept clearly, using simple examples and analogies appropriate for the target audience (Child, Beginner, College Student, or Professional).""",

    "roadmap_planner.md": """You are an expert Roadmap Planner Agent.
Your task is to generate a personalized learning roadmap.

Topic: {{ topic }}
Duration: {{ duration_weeks }} weeks
Daily Study Hours: {{ daily_hours }} hours

Provide:
1. A Weekly Learning Plan
2. Key Milestones
3. Recommended Resources (Books, courses, websites)""",

    "formula_sheet_generator.md": """You are an expert Formula Sheet Generator Agent.
Your task is to generate a comprehensive formula sheet.

Subject: {{ subject }}
Specific Topic: {{ specific_topic }}

For each formula, provide:
- The Formula
- Meaning of all variables
- A quick Example of how to use it""",

    "viva_preparation.md": """You are an expert Viva Preparation Agent.
Your task is to generate oral examination (viva) questions.

Topic: {{ topic }}
Level: {{ level }}

For each question, provide:
- The Question
- Expected Answer
- Potential Follow-up Questions""",

    "revision_planner.md": """You are an expert Revision Planner Agent.
Your task is to create a revision schedule leading up to an exam.

Exam Date: {{ exam_date }}
Subjects: {{ subjects }}
Daily Study Hours: {{ daily_study_hours }}

Output:
1. Day-wise Revision Plan
2. Priority Topics to focus on
3. Mock Test Schedule"""
}

os.makedirs('backend/prompts/student_assistant', exist_ok=True)
for filename, content in prompts.items():
    with open(f"backend/prompts/student_assistant/{filename}", 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated 10 student assistant prompts!")
