from google.adk.sessions import InMemorySessionService
from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.genai import types  # For creating message Content/Parts
import asyncio
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / "my_travel_planner" / ".env")  # Load environment variables from the .env file
from my_travel_planner.agent import get_root_agent

APP_NAME = "travel-planner_app"
USER_ID = "user_1"
SESSION_ID = "session_001"


async def setup_session_and_runner(root_agent: Agent = None, session_id: str = SESSION_ID):
    # Setup Runner for execution
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=session_id)
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
    return session, runner


async def call_agent_async(query: str, root_agent: Agent = None, session_id: str = SESSION_ID) -> str:
    content = types.Content(role='user', parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner(root_agent=root_agent, session_id=session_id)
    events = runner.run_async(user_id=USER_ID, session_id=session_id, new_message=content)
    final_response_text = "No response received."
    async for event in events:
        # Key Concept: is_final_response() marks the concluding message for the turn.
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break

    print(f"<<< Agent Response: {final_response_text}")
    return final_response_text


async def run_agent_pipeline(query: str) -> str:
    root_agent = get_root_agent()
    return await call_agent_async(query=query, root_agent=root_agent, session_id=SESSION_ID)


if __name__ == "__main__":
    user_query = ("I'm planning a trip to Paris in the spring. What are some must-see attractions and local events "
                  "during that time?")
    asyncio.run(run_agent_pipeline(query=user_query))
