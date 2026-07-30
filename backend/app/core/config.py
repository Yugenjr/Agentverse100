from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY_1: str = ""
    GROQ_API_KEY_2: str = ""
    GROQ_API_KEY_3: str = ""
    GROQ_API_KEY_4: str = ""
    GROQ_API_KEY_5: str = ""
    GROQ_API_KEY_6: str = ""
    GROQ_API_KEY_7: str = ""
    GROQ_API_KEY_8: str = ""
    GROQ_API_KEY_9: str = ""
    GROQ_API_KEY_10: str = ""
    LLM_MODEL: str = "llama3-70b-8192"

    class Config:
        env_file = "../.env"

settings = Settings()
