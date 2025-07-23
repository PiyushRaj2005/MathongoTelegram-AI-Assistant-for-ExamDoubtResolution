import json
import os

def get_fallback_response(query: str) -> str:
    fallback_path = os.path.join("prompts", "fallback.json")
    try:
        with open(fallback_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get(query.lower(), "Sorry, couldn't find an answer. Try rephrasing.")
    except:
        return "Sorry, couldn't load fallback data."
