from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.routes import router as api_router
from app.registry.agent_registry import registry

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Autodiscover agents
    registry.autodiscover()
    yield
    # Shutdown
    pass

app = FastAPI(title="AgentVerse-100 API", lifespan=lifespan)

# Setup CORS for the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For dev purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to AgentVerse-100 API", "status": "online"}
