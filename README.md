# Travel Planner AI

A workshop-ready starter kit for building a travel planning agent with **Google ADK**, **Gemini**, and **FastAPI** — used in the *Building Production-Ready AI Systems in Python with Google ADK* session. Core files now contain TODO-guided placeholders for participants to complete during the lab.

---

## Stack

| Layer | Technology |
|---|---|
| Agent framework | [Google ADK](https://google.github.io/adk-docs/) |
| LLM | Gemini 2.5 Flash |
| API server | FastAPI + Uvicorn |
| Dependency management | [uv](https://docs.astral.sh/uv/) |

---

## Project Structure

```
google-adk/
├── my_travel_planner/
│   ├── agent.py          # Root agent definition
│   └── .env              # API keys (not committed)
├── run.py                # Agent runner & session setup
├── api.py                # FastAPI endpoint
└── pyproject.toml        # Project dependencies
```

---

## Workshop TODOs

1. Update `my_travel_planner/agent.py` with a fully configured `google.adk.agents.Agent` (model, description, instructions, and optional tools).
2. Implement the session + runner wiring plus response streaming logic in `run.py` (`setup_session_and_runner`, `call_agent_async`, `run_agent_pipeline`).
3. Wire the `/ask` FastAPI route in `api.py` to await `run_agent_pipeline()` and return the agent's reply.

Everything else (environment loading, dependency scaffolding, and data models) is already in place so you can focus on the agent logic during the workshop.

---

## Getting Started

### 1. Prerequisites

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install Dependencies

Clone the repo and run:

```bash
uv sync
```

This creates a `.venv` virtual environment and installs all dependencies from `pyproject.toml`.

---

### 3. Set Up Environment Variables

Create the `.env` file inside `my_travel_planner/`:

```bash
touch my_travel_planner/.env
```

Add your Gemini API key to it:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

> Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).

---

### 4. Run the FastAPI Server

```bash
uv run uvicorn api:app --reload
```

The server starts at **`http://localhost:8000`**.

- Interactive docs (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 5. Query the Agent

Once you've filled in the workshop TODOs, try hitting the API.

**Using `curl`:**

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "Best things to do in Paris in spring?"}'
```

**Example response (after completing the TODOs):**

```json
{
  "query": "Best things to do in Paris in spring?",
  "response": "Paris in spring is magical! Here are some must-dos: ..."
}
```

---

### Run Without the API (Script Only)

You can also run the agent directly from the terminal once the TODOs are implemented:

```bash
uv run python run.py
```
