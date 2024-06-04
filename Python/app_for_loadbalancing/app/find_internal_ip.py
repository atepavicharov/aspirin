import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    internal_ip = s.getsockname()[0]
    s.close()
    return internal_ip


if __name__ == '__main__':
    print('Internal IP:', get_ip())
