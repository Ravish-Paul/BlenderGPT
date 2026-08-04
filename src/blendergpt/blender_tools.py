import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)


def create_cube(size, x, y, z):
    bpy.ops.mesh.primitive_cube_add(size=size, enter_editmode=False, align='WORLD', scale=(x, y, z))


def create_sphere(radius, x, y, z):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, enter_editmode=False, align='WORLD', scale=(x, y, z))
