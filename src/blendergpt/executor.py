from blendergpt.tool_registry import TOOLS


def execute(command):
    tools_name = command["tool"]

    function = TOOLS.get(tools_name)

    if function is None:
        return {"status": False, "error": "Unknown tool"}

    else:
        parameters = command.copy()
        del parameters["tool"]
        return function(**parameters)