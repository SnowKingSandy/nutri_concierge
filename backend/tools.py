import json
from google.adk.tools.function_tool import FunctionTool
from .nutrition_api import search_food  # Changed import

# -----------------------------
# MACRO CALCULATOR
# -----------------------------
def calculate_macros(foods: list) -> str:
    total = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}

    for f in foods:
        n = f.get("nutrients", {})
        total["calories"] += n.get("ENERC_KCAL", 0)
        total["protein"]  += n.get("PROCNT", 0)
        total["fat"]      += n.get("FAT", 0)
        total["carbs"]    += n.get("CHOCDF", 0)

    return json.dumps({"success": True, "macros": total}, indent=2)

# -----------------------------
# COMPARISON TOOL
# -----------------------------
def compare_foods(f1, f2) -> str:
    return json.dumps({
        "food1": f1["label"],
        "food2": f2["label"],
        "differences": {
            "calories": f1["nutrients"]["ENERC_KCAL"] - f2["nutrients"]["ENERC_KCAL"],
            "protein":  f1["nutrients"]["PROCNT"] - f2["nutrients"]["PROCNT"],
            "carbs":    f1["nutrients"]["CHOCDF"] - f2["nutrients"]["CHOCDF"],
            "fat":      f1["nutrients"]["FAT"] - f2["nutrients"]["FAT"]
        }
    }, indent=2)

# -----------------------------
# MEAL PLANNER TOOL
# -----------------------------
def meal_planner(goal: str) -> str:
    # Updated to use search_food instead of edamam_search_food
    data = json.loads(search_food(goal))
    foods = data.get("foods", [])[:3]
    return json.dumps({"goal": goal, "meal": foods}, indent=2)

# -----------------------------
# ADK TOOL WRAPPERS
# -----------------------------
# Renamed tool for clarity
nutrition_search_tool = FunctionTool(search_food)
calculate_macros_tool = FunctionTool(calculate_macros)
compare_tool          = FunctionTool(compare_foods)
meal_planner_tool     = FunctionTool(meal_planner)
