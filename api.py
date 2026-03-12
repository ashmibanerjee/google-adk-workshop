from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / "my_travel_planner" / ".env")

from run import run_agent_pipeline

app = FastAPI(title="Travel Planner AI", description="Powered by Google ADK + Gemini")


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    query: str
    response: str


@app.post("/ask", response_model=QueryResponse)
async def ask_agent(request: QueryRequest):
    """Workshop TODO: call run_agent_pipeline() once the agent + runner are implemented."""
    raise NotImplementedError(
        "Replace this stub by awaiting run_agent_pipeline(query=request.query) and returning a QueryResponse with "
        "the agent's answer."
    )
