import sys
import socket

host = ""
port = 7777

def Serveur():
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    msg = ""
    reply = ""
    while msg != "kill":
        print("En attente du client")
        conn, address = server_socket.accept()
        print(f"Client connecté {address}")

        msg = ""
        while msg != "kill" and msg != "disconect" and msg != "reset":
            msg = conn.recv(1024).decode()
            print(msg)
            reply = msg
            conn.send(reply.encode())



        conn.close()
        print("fermeture de la connexion")

    server_socket.close()
    print("fermeture du serveur")


if __name__ == '__main__':
    sys.exit(Serveur())