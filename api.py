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
    response = await run_agent_pipeline(query=request.query)
    return QueryResponse(query=request.query, response=response)

