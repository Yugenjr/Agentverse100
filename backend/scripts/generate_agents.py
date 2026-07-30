import os
import json

CATEGORIES = [
    "Text Processing",
    "Programming",
    "Student Assistant",
    "Business",
    "Data Science",
    "Cyber Security",
    "Productivity",
    "Creative",
    "DevOps",
    "AI Utilities"
]

# Simple template for an agent
AGENT_TEMPLATE = """from app.agents.base import BaseAgent
from app.schemas.models import AgentOutput
from app.core.groq_service import groq_service

class {class_name}(BaseAgent):
    name = "{name}"
    description = "{description}"
    category = "{category}"
    icon = "{icon}"
    system_prompt = \"\"\"{system_prompt}\"\"\"

    async def execute(self, input_data: str) -> AgentOutput:
        user_prompt = f"Input: {{input_data}}"
        response = await groq_service.generate_response(self.system_prompt, user_prompt)
        return response
"""

# Let's generate 10 agents for each category
AGENTS_DATA = {
    "Text Processing": [
        ("Summarizer", "Condenses long text into key points.", "FileText", "You are an expert summarizer. Summarize the text provided."),
        ("Grammar Fixer", "Corrects grammar and spelling mistakes.", "CheckSquare", "You are an expert proofreader. Fix any grammatical errors."),
        ("Translator", "Translates text to another language.", "Globe", "You are a professional translator. Translate the text accurately."),
        ("Paraphraser", "Rewrites text in a different way.", "RefreshCw", "You are an expert at paraphrasing. Rewrite the input text."),
        ("Tone Adjuster", "Changes the tone of the text.", "Sliders", "Adjust the tone of the text as requested (e.g., more professional, friendly)."),
        ("Keyword Extractor", "Extracts key terms from text.", "Key", "Extract the top keywords from the provided text."),
        ("Sentiment Analyzer", "Determines the sentiment of text.", "Smile", "Analyze the text and determine if the sentiment is positive, negative, or neutral."),
        ("Text Expander", "Expands brief notes into full sentences.", "Maximize", "Expand the short notes into a comprehensive paragraph."),
        ("Readability Scorer", "Calculates readability and suggests improvements.", "BookOpen", "Analyze the readability of the text and suggest how to make it clearer."),
        ("Entity Recognizer", "Extracts named entities (people, places, orgs).", "UserPlus", "Extract all Named Entities from the text.")
    ],
    "Programming": [
        ("Code Explainer", "Explains complex code snippets.", "Code", "Explain the following code step by step."),
        ("Bug Finder", "Identifies potential bugs in code.", "Bug", "Analyze the code and identify any potential bugs or edge cases."),
        ("Code Refactorer", "Improves code quality and structure.", "Wrench", "Refactor the provided code to follow best practices and improve readability."),
        ("Unit Test Generator", "Generates unit tests for functions.", "TestTube", "Write comprehensive unit tests for the provided code."),
        ("Docstring Writer", "Adds docstrings to functions/classes.", "AlignLeft", "Write detailed docstrings for the provided Python code using Google style."),
        ("Regex Builder", "Creates regular expressions from descriptions.", "Hash", "Provide a regex pattern that matches the user's description."),
        ("SQL Optimizer", "Optimizes SQL queries for performance.", "Database", "Analyze and optimize the provided SQL query."),
        ("Code Converter", "Translates code from one language to another.", "Repeat", "Translate the provided code to the language requested."),
        ("Algorithm Designer", "Designs algorithms for specific problems.", "Cpu", "Provide an algorithmic solution (with pseudocode) for the given problem."),
        ("Git Command Helper", "Suggests git commands for workflows.", "GitCommit", "Provide the correct git commands to achieve the user's workflow.")
    ],
    "Student Assistant": [
        ("Math Solver", "Solves math problems with step-by-step reasoning.", "Calculator", "Solve the math problem step by step."),
        ("Essay Planner", "Creates outlines for essays.", "Edit3", "Provide a structured outline for an essay based on the topic."),
        ("Flashcard Creator", "Generates flashcards from study notes.", "Layers", "Create question/answer flashcards based on the notes."),
        ("History Tutor", "Answers historical questions.", "Clock", "You are an expert history tutor. Answer the questions accurately."),
        ("Science Explainer", "Explains scientific concepts simply.", "Activity", "Explain the scientific concept as if to a high school student."),
        ("Citation Generator", "Generates academic citations.", "Bookmark", "Format the provided source into APA and MLA citations."),
        ("Study Schedule Planner", "Creates realistic study schedules.", "Calendar", "Create a structured study schedule based on the topics and time available."),
        ("Grammar Tutor", "Explains grammar rules with examples.", "Feather", "Explain the grammar rule in question and provide examples."),
        ("Debate Prep", "Provides arguments for both sides of a topic.", "MessageCircle", "Provide strong arguments for and against the given topic."),
        ("Vocabulary Builder", "Suggests synonyms and word usages.", "Type", "Provide synonyms, antonyms, and example sentences for the word.")
    ],
    "Business": [
        ("Email Drafter", "Drafts professional business emails.", "Mail", "Draft a professional business email based on the prompt."),
        ("Meeting Summarizer", "Summarizes meeting transcripts.", "Users", "Extract action items and key decisions from the meeting transcript."),
        ("Pitch Deck Helper", "Suggests structure for pitch decks.", "Presentation", "Create a slide-by-slide outline for a pitch deck."),
        ("SWOT Analyzer", "Performs SWOT analysis on a business idea.", "Crosshair", "Conduct a Strengths, Weaknesses, Opportunities, and Threats analysis."),
        ("Market Researcher", "Provides high-level market trends.", "TrendingUp", "Summarize current market trends for the specified industry."),
        ("Job Description Writer", "Writes professional job postings.", "Briefcase", "Write a compelling job description based on the title and requirements."),
        ("Interview Prep", "Generates interview questions.", "Mic", "Generate 5 behavioral and 5 technical interview questions for the role."),
        ("Performance Reviewer", "Helps draft performance reviews.", "Star", "Draft a constructive and professional performance review."),
        ("Negotiation Coach", "Provides tips for business negotiations.", "Handshake", "Provide strategic advice for negotiating the specified scenario."),
        ("Brand Namer", "Brainstorms brand names and taglines.", "Tag", "Generate 10 catchy brand names and taglines for the business idea.")
    ],
    "Data Science": [
        ("Pandas Helper", "Generates pandas code for data manipulation.", "Table", "Provide pandas code to achieve the data manipulation described."),
        ("Data Cleaner", "Suggests steps to clean dirty datasets.", "Trash2", "Outline the steps required to clean and preprocess the described dataset."),
        ("Chart Recommender", "Suggests the best visualization for data.", "BarChart2", "Recommend the best chart types for visualizing this data and explain why."),
        ("Stats Explainer", "Explains statistical concepts clearly.", "PieChart", "Explain the statistical concept in an easy-to-understand way."),
        ("Model Selector", "Recommends machine learning models.", "Box", "Recommend the best machine learning algorithms for this specific problem."),
        ("Feature Engineer", "Suggests new features from existing data.", "Zap", "Suggest new features that could be engineered from the provided dataset."),
        ("Hypothesis Tester", "Helps design statistical tests.", "HelpCircle", "Design a hypothesis test (Null, Alternative, test statistic) for the scenario."),
        ("Regex for Data", "Writes regex to extract data from text.", "Filter", "Provide the exact regex pattern to extract the requested data."),
        ("SQL to Pandas", "Converts SQL queries to Pandas syntax.", "Shuffle", "Convert the provided SQL query into equivalent Pandas syntax."),
        ("Metrics Explainer", "Explains ML evaluation metrics.", "Target", "Explain what the given ML evaluation metric means and when to use it.")
    ],
    "Cyber Security": [
        ("Vulnerability Scanner", "Identifies common security flaws.", "Shield", "Analyze the code/description for common security vulnerabilities (e.g., OWASP top 10)."),
        ("Password Policy Maker", "Generates strong password policies.", "Lock", "Draft a comprehensive password policy for an organization."),
        ("Phishing Analyzer", "Analyzes emails for phishing signs.", "AlertTriangle", "Analyze the provided email text and highlight potential phishing indicators."),
        ("Encryption Explainer", "Explains cryptographic algorithms.", "Key", "Explain how the specified encryption algorithm works in simple terms."),
        ("Firewall Rule Generator", "Helps write iptables/firewall rules.", "Server", "Provide the exact firewall rules to achieve the requested network policy."),
        ("Incident Response Planner", "Drafts IR playbooks.", "Clipboard", "Create an incident response playbook for the specified security event."),
        ("Risk Assessor", "Calculates security risks based on impact.", "AlertOctagon", "Perform a qualitative risk assessment for the described scenario."),
        ("Compliance Checker", "Checks requirements for SOC2/GDPR.", "CheckCircle", "Explain the requirements for the specified compliance framework."),
        ("Log Analyzer", "Finds anomalies in log excerpts.", "Terminal", "Analyze the log snippet and identify any suspicious activity."),
        ("Secure Coding Guide", "Provides secure coding practices.", "ShieldCheck", "Provide secure coding guidelines for the specified language.")
    ],
    "Productivity": [
        ("Task Prioritizer", "Organizes tasks using frameworks like Eisenhower.", "List", "Categorize the provided tasks using the Eisenhower Matrix."),
        ("Pomodoro Planner", "Creates custom Pomodoro schedules.", "Clock", "Create a detailed Pomodoro schedule based on the user's tasks and time."),
        ("Habit Tracker", "Suggests habit loops and routines.", "CheckSquare", "Design a daily routine and habit loop for the specified goal."),
        ("Goal Setter", "Helps set SMART goals.", "Target", "Convert the user's vague goal into a SMART goal."),
        ("Meeting Agenda Maker", "Drafts clear agendas for meetings.", "FileText", "Create a structured meeting agenda based on the topics."),
        ("Inbox Zero Helper", "Categorizes unorganized email text.", "Mail", "Suggest folders or actions (Reply, Delegate, Delete) for the email summaries."),
        ("Morning Routine", "Suggests optimal morning routines.", "Sunrise", "Design a morning routine based on the user's preferences."),
        ("Distraction Blocker", "Provides tips to avoid specific distractions.", "XOctagon", "Provide actionable advice to overcome the specific distraction."),
        ("Time Auditor", "Analyzes how time was spent.", "PieChart", "Analyze the time log and provide insights on productivity leaks."),
        ("Delegation Matrix", "Helps decide what to delegate.", "Users", "Analyze the tasks and identify which ones should be delegated.")
    ],
    "Creative": [
        ("Story Generator", "Generates creative short stories.", "Book", "Write a creative and engaging short story based on the prompt."),
        ("Character Creator", "Builds detailed fictional characters.", "User", "Create a detailed character profile including backstory, motivations, and flaws."),
        ("Poem Writer", "Writes poems in various styles.", "Feather", "Write a poem in the requested style about the given topic."),
        ("World Builder", "Fleshes out fictional worlds.", "Globe", "Describe the geography, culture, and magic/tech system of a fictional world."),
        ("Dialogue Writer", "Writes engaging dialogue between characters.", "MessageSquare", "Write a dialogue snippet between two characters in the given scenario."),
        ("Joke Generator", "Tells jokes on specific topics.", "Smile", "Write a clever joke or pun about the requested topic."),
        ("Song Lyricist", "Writes lyrics for songs.", "Music", "Write a verse and chorus for a song based on the theme."),
        ("Game Idea Generator", "Brainstorms video game concepts.", "Play", "Generate a unique concept for a video game including mechanics and story."),
        ("Plot Twist Maker", "Suggests surprising plot twists.", "Shuffle", "Suggest 3 surprising but logical plot twists for the story summary."),
        ("Name Generator", "Generates fantasy or sci-fi names.", "Tag", "Generate 10 unique names suitable for the requested setting.")
    ],
    "DevOps": [
        ("Dockerfile Generator", "Writes Dockerfiles for applications.", "Box", "Write an optimized Dockerfile for the specified application stack."),
        ("CI/CD Planner", "Designs CI/CD pipelines.", "GitMerge", "Design a CI/CD pipeline workflow for the given project."),
        ("K8s Manifest Writer", "Generates Kubernetes YAMLs.", "Layers", "Write the required Kubernetes manifests (Deployment, Service, etc.) for the app."),
        ("Terraform Builder", "Creates Terraform scripts.", "Cloud", "Write Terraform code to provision the requested cloud infrastructure."),
        ("Cron Schedule Maker", "Explains and generates cron expressions.", "Clock", "Provide the cron expression for the requested schedule and explain it."),
        ("Nginx Configurator", "Writes Nginx server blocks.", "Server", "Write an Nginx configuration file for the specified routing requirements."),
        ("Log Rotate Guide", "Explains how to set up log rotation.", "RotateCcw", "Explain how to configure logrotate for the specified log files."),
        ("Bash Script Writer", "Writes shell scripts for automation.", "Terminal", "Write a robust bash script to automate the requested task."),
        ("Monitoring Alert Config", "Drafts Prometheus alert rules.", "Bell", "Write Prometheus alerting rules for the specified metrics."),
        ("Cloud Cost Optimizer", "Suggests ways to reduce cloud bills.", "DollarSign", "Suggest architectural changes to reduce costs for the described cloud setup.")
    ],
    "AI Utilities": [
        ("Prompt Improver", "Refines prompts for better LLM outputs.", "Edit", "Rewrite the user's prompt to be more detailed, clear, and effective for an LLM."),
        ("System Prompt Builder", "Generates system prompts for new agents.", "Cpu", "Draft a comprehensive system prompt for the described AI persona."),
        ("Token Estimator", "Estimates token counts (conceptual).", "Hash", "Estimate the relative token size of the text and explain tokenization concepts."),
        ("Few-Shot Generator", "Creates few-shot examples for prompts.", "List", "Generate 3 diverse input/output examples for the specified task."),
        ("Hallucination Checker", "Identifies potential factual errors.", "Eye", "Review the text and highlight statements that might be AI hallucinations requiring verification."),
        ("Persona Adopter", "Adopts any persona requested.", "UserCheck", "Adopt the requested persona and respond entirely in character."),
        ("Format Converter", "Converts between JSON/XML/YAML/CSV.", "File", "Convert the provided data structure into the requested format (e.g., JSON to YAML)."),
        ("JSON Schema Generator", "Generates JSON schemas from examples.", "Code", "Create a valid JSON schema that matches the provided JSON data."),
        ("Embeddings Explainer", "Explains vector embeddings simply.", "Compass", "Explain how vector embeddings work and how they relate to the prompt."),
        ("RAG Query Optimizer", "Optimizes search queries for RAG.", "Search", "Rewrite the user query to maximize retrieval success in a vector database.")
    ]
}

def to_class_name(name: str) -> str:
    return name.replace(" ", "").replace("/", "") + "Agent"

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'app', 'agents', 'categories')
    os.makedirs(base_dir, exist_ok=True)

    # Need a __init__.py in categories
    open(os.path.join(base_dir, '__init__.py'), 'w').close()

    total_agents = 0
    for category_name, agents in AGENTS_DATA.items():
        cat_folder = category_name.lower().replace(" ", "_")
        cat_path = os.path.join(base_dir, cat_folder)
        os.makedirs(cat_path, exist_ok=True)
        open(os.path.join(cat_path, '__init__.py'), 'w').close()

        for name, desc, icon, prompt in agents:
            class_name = to_class_name(name)
            file_name = class_name.lower() + ".py"
            file_path = os.path.join(cat_path, file_name)

            content = AGENT_TEMPLATE.format(
                class_name=class_name,
                name=name,
                description=desc,
                category=category_name,
                icon=icon,
                system_prompt=prompt
            )

            with open(file_path, 'w') as f:
                f.write(content)
            total_agents += 1

    print(f"Successfully generated {total_agents} agents across {len(AGENTS_DATA)} categories!")

if __name__ == "__main__":
    main()
