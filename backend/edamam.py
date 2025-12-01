import requests
import json
from .config import EDAMAM_APP_ID, EDAMAM_APP_KEY

EDAMAM_URL = "https://api.edamam.com/api/food-database/v2/parser"

def edamam_search_food(query: str) -> str:
    params = {
        "app_id": EDAMAM_APP_ID,
        "app_key": EDAMAM_APP_KEY,
        "ingr": query,
    }

    res = requests.get(EDAMAM_URL, params=params)

    if res.status_code != 200:
        return json.dumps({"success": False, "error": "API Error"})

    out = []
    data = res.json()

    for hint in data.get("hints", []):
        f = hint["food"]
        out.append({
            "label": f["label"],
            "category": f.get("category", "Unknown"),
            "nutrients": f.get("nutrients", {})
        })

    return json.dumps({"success": True, "foods": out}, indent=2)
