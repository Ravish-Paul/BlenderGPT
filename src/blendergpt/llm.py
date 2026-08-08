from blendergpt.tool_definitions import TOOLS
from blendergpt.config import MODEL, GEMINI_API_KEY
from blendergpt.parser import parse_response
from google import genai


def available_tools():
    lines = []
    for key, val in TOOLS.items():
        lines.append(f"Tool: {key}\n\n")
        lines.append(f"Description:\n{val['description']}\n\n")
        lines.append("Parameters:\n\n" if val['parameters'] else "")

        for key1, val1 in val['parameters'].items():
            lines.append(f"-{key1}\n")
            lines.append(f" Type: {val1['type']}\n")
            lines.append(f" Required: {val1['required']}\n")
            lines.append(f" Description: {val1['description']}\n\n")

    return "\n".join(lines)


def build_system_prompt():

    system_prompt = f"""You are an AI assistant that converts natural language into Blender tool calls.

Rules:

1. Respond ONLY with valid JSON.
2. Never explain your reasoning.
3. Never use Markdown.
4. Use only the available tools.
5. Return exactly one JSON object.
6. If the request cannot be completed, return an error JSON.

{available_tools()}

""""""Return exactly this structure:

{
  "tool": "tool_name",
  "parameters": {
      ...
  }
}

Do not return "tool_name".
Do not return "tool_code".
Do not write function calls.
Do not write Python code.

Example:

User:
Create a cube of size 2 at location 1, 0, 0

Response:
{
  "tool": "create_cube",
  "parameters": {
    "size": 2,
    "location": [1, 0, 0]
  }
}""""""
""" 

    return system_prompt


def call_llm(system_prompt: str, user_prompt: str) -> str:
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model=MODEL,
        contents=f"System Prompt: {system_prompt}\n\nUser Prompt: {user_prompt}"
    )
    return response.text

def generate_command(user_prompt):
    pass

response = call_llm(system_prompt=build_system_prompt(), user_prompt="Create a cube of size 4 at location 1, 0, 0")

print(parse_response(response.text))
