# AgentVerse-100

A sprawling Multi-Agent AI Platform built with a modern Next.js 15 frontend and a highly scalable FastAPI Python backend. Powered by the Groq API for lightning-fast inference.

## Features

- **100 Specialized Agents**: Precisely 100 AI agents grouped logically into 10 categories (e.g., Data Science, Cyber Security, Business, Productivity).
- **Execution Engine**: Robust backend execution that measures performance and captures detailed logs.
- **Category Runner**: Leverage `asyncio` to execute all 10 agents within a category concurrently.
- **Pipeline Builder**: A drag-and-drop style visual builder to chain multiple agents sequentially (e.g., Summarizer → Translator → Email Drafter).
- **Premium Aesthetics**: Dark theme, glassmorphism, Framer Motion animations, and shadcn/ui components.

## Architecture

* **Frontend**: Next.js 15 (App Router), TypeScript, TailwindCSS, shadcn/ui.
* **Backend**: FastAPI, Python 3.12, Pydantic, AsyncIO.
* **LLM Core**: Centralized Groq inference service using `llama3-70b-8192` (configurable).

## Installation Guide

### Prerequisites
- Node.js 18+
- Python 3.12+
- Groq API Key

### Backend Setup

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic pydantic-settings groq rich python-dotenv
   ```
4. Configure `.env`:
   Open `backend/.env` and add your Groq API Key:
   ```
   GROQ_API_KEY=your_key_here
   LLM_MODEL=llama3-70b-8192
   ```
5. Generate the 100 Agents:
   ```bash
   python scripts/generate_agents.py
   ```
6. Start the server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the Next.js development server:
   ```bash
   npm run dev
   ```
4. Open `http://localhost:3000` in your browser.

## Roadmap
- [ ] Add vector database for RAG capabilities.
- [ ] Implement user authentication and execution history.
- [ ] Add parallel branches to the Pipeline Builder.

## License
MIT
