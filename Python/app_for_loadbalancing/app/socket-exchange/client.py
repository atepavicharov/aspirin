import socket


def send(msg):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    clientsocket.send(bytes(msg, 'UTF-8'))
    clientsocket.close()
