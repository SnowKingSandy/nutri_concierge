import openfoodfacts
import json

def search_food(query: str) -> str:
    # Initialize API with a User-Agent (Required by OpenFoodFacts)
    api = openfoodfacts.API(user_agent="NutriConcierge/1.0")
    
    try:
        # Search the database
        results = api.product.text_search(query)
        
        out = []
        products = results.get("products", [])
        
        for p in products:
            # Skip items without nutrition info
            if "nutriments" not in p:
                continue
                
            n = p["nutriments"]
            
            # Map OpenFoodFacts keys to the Edamam-style keys your UI expects
            mapped_food = {
                "label": p.get("product_name", "Unknown Product"),
                "category": p.get("categories", "Unknown").split(',')[0], # Take first category
                "nutrients": {
                    "ENERC_KCAL": n.get("energy-kcal_100g", 0),
                    "PROCNT": n.get("proteins_100g", 0),
                    "FAT": n.get("fat_100g", 0),
                    "CHOCDF": n.get("carbohydrates_100g", 0)
                }
            }
            out.append(mapped_food)
            
            # Limit to top 5 results to keep response size manageable
            if len(out) >= 5:
                break

        return json.dumps({"success": True, "foods": out}, indent=2)

    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})
