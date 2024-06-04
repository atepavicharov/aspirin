import socket

# based on https://stackoverflow.com/questions/7749341/basic-python-client-socket-example
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections

print('Listening for messages')
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(1024)
    if len(buf) > 0:
        print(str(buf))
