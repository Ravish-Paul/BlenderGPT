import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)

    return bpy.context.object.name


def create_cube(size, location):
    x, y, z = location

    bpy.ops.mesh.primitive_cube_add(size=size, enter_editmode=False, align='WORLD', location=(x, y, z))


    return bpy.context.object.name


def create_sphere(radius, location):
    x, y, z = location

    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, enter_editmode=False, align='WORLD', location=(x, y, z))

    return bpy.context.object.name