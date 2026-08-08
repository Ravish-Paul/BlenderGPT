import sys
from pathlib import Path

SRC_DIR = Path(r"E:\blendergpt\src")

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


from blendergpt.blender_executor import execute


import socket
import json
import threading
import queue
import bpy


HOST = "127.0.0.1"
PORT = 5000

command_queue = queue.Queue()


def receive_commands():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Blender server listening on {HOST}:{PORT}")

    while True:
        connection, address = server.accept()

        print(f"Client connected: {address}")

        data = connection.recv(4096)

        if data:
            command = json.loads(data.decode("utf-8"))
            command_queue.put((command, connection))


def process_commands():
    while not command_queue.empty():

        command, connection = command_queue.get()

        print("Received command:", command)

        try:
            from blendergpt.blender_executor import execute

            print("Executing command...")

            result = execute(command)

            print("Execution result:", result)

            response = {
                "status": True,
                "result": result
            }

        except Exception as e:

            print("Execution error:", repr(e))

            response = {
                "status": False,
                "error": str(e)
            }

        try:
            connection.sendall(
                json.dumps(response).encode("utf-8")
            )

            print("Response sent:", response)

        except Exception as e:
            print("Response error:", repr(e))

        finally:
            connection.close()

    return 0.1


def start_server():

    thread = threading.Thread(
        target=receive_commands,
        daemon=True
    )

    thread.start()

    bpy.app.timers.register(
        process_commands,
        first_interval=0.1
    )

    print("BlenderGPT server started.")


start_server()