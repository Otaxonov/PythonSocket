import socket

IP = "127.0.0.1"
PORT = 10000
HOST = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(HOST)

server.listen()

print('I\'m listening your connections')

while True:
    connection, address = server.accept()
    print(f"Connected to {address}")

    message = b'Hello, World!'
    connection.send(message)
