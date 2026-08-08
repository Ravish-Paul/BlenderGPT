from blendergpt.tool_registry import TOOLS

def execute(command):

    tools_name = command["tool"]

    tool = TOOLS.get(tools_name)

    if tool is None:
        return {"status": False, "error": "Unknown tool"}

    parameters = command['parameters']
    
    return tool(**parameters)
