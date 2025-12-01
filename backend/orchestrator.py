from google.adk.agents import SequentialAgent
from .agents import nutrition_search_agent, meal_planner_agent

coordinator_agent = SequentialAgent(
    name="coordinator",
    sub_agents=[nutrition_search_agent, meal_planner_agent]
)
