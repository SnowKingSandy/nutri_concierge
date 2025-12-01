from google.adk.agents import Agent
from .config import MODEL_NAME
from .tools import (
    nutrition_search_tool, meal_planner_tool,
    calculate_macros_tool, compare_tool
)

# -----------------------------
# SEARCH AGENT
# -----------------------------
nutrition_search_agent = Agent(
    name="search_agent",
    model=MODEL_NAME,
    instruction="Use search_food to find nutritional information for foods.",
    tools=[nutrition_search_tool],
    output_key="foods"
)

# -----------------------------
# MEAL PLANNER AGENT
# -----------------------------
meal_planner_agent = Agent(
    name="meal_agent",
    model=MODEL_NAME,
    instruction="Use meal_planner to generate meals.",
    tools=[meal_planner_tool],
    output_key="meal_plan"
)
