import json

def parse_response(response: str):
    try:
        data = json.loads(response)
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"

    if not isinstance(data, dict):
        return False, f"Response must be an object"

    return True, data
