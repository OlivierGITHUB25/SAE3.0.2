import sys
import socket


host = "192.168.75.1"
port = 7777

def Client():
    client_socket = socket.socket()
    client_socket.connect((host, port))
    msg = ""

    while msg != "exit" and msg != "bye":
        msg = input("envoyé:")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        print(data)

    client_socket.close()

if __name__ == '__main__':
    sys.exit(Client())