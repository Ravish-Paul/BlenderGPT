from blendergpt.tool_definitions import TOOLS

TYPE_MAP ={
    "number" : (int, float),
    "array"  : list,
    "string" : str,
    "tuple" : list
}

def validate_command(command):
    try:
        if not isinstance(command, dict):
            raise ValueError("command must be a dictionary")
        
        if "tool" not in command:
            raise ValueError("tool must exist")

        tool_name = command["tool"]
        if tool_name not in TOOLS:
            raise ValueError("tool must be registered")

        if 'parameters' not in command:
            raise ValueError("parameters must exist")

        parameters = command['parameters']

        if not isinstance(parameters, dict):
            raise ValueError("Parameters must be a dictionary")

        for key, val in TOOLS[tool_name]['parameters'].items():
            if val['required']:
                if key not in parameters:
                    raise ValueError(f"parameters {key} not in json")
                type_val = val['type']
                expected_type = TYPE_MAP[type_val]
                if not isinstance(parameters[key], expected_type):
                    raise ValueError(f"parameters {key} must be {type_val}")
                

    except ValueError as e:
        return False, str(e)

    return True, command
