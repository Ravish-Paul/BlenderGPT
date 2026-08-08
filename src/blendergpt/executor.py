import socket
import json


HOST = "127.0.0.1"
PORT = 5000


def execute(command):

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client.connect((HOST, PORT))

    client.sendall(
        json.dumps(command).encode("utf-8")
    )

    response = client.recv(4096)

    client.close()

    return json.loads(response.decode("utf-8"))