TOOLS = {
    "clear_scene": {
        "description": "delete all objects from blender scene.",
        "parameters": {}
    },
    "create_cube": {
        "description": "create a cube in blender scene.",
        "parameters": {
            "size": {
                "type": "number",
                "required": True,
                "description": "Length of each side."
            },
            "location": {
                "type": "tuple",
                "required": True,
                "description": "World coordinates. (x, y, z)"
            }
        }
    },
    "create_sphere": {
        "description": "create a sphare in blender scene.",
        "parameters": {
            "radius": {
                "type": "number",
                "required": True,
                "description": "Length of redius of sphare."
            },
            "location": {
                "type": "tuple",
                "required": True,
                "description": "World coordinates. (x, y, z)"
            }
        }
    }
}