from tool_registry import TOOLS

def build_system_prompt():
    systme_prompt = f"""you are a professional blender speliest.
    available tools are.
    {TOOLS.values}""" 

    return systme_prompt

