import socket

IP = "127.0.0.1"
PORT = 10000
HOST = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(HOST)

while True:
    message = client.recv(1024)
    print(message.decode('utf-8'))

    break
