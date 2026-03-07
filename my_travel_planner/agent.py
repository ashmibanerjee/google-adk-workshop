from google.adk.agents import Agent


def get_root_agent():
    # The Root Agent (The "Brain")
    travel_planner = Agent(
        name="travel_planner",
        model="gemini-2.5-flash",
        description="A comprehensive travel planning assistant.",
        instruction="""You are a world-class travel planner.
        Recommend places to visit based on the user's query.""",
    )
    return travel_planner


root_agent = get_root_agent()
