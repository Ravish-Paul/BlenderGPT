from blendergpt.llm import generate_command
from blendergpt.executor import execute

def run(user_prompt):
    command= generate_command(user_prompt=user_prompt)
    result = execute(command)

    return result

print(run("Create a sphare of radius 6 at 1,0,0"))